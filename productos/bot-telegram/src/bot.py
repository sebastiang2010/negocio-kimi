import logging

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from .announce import Announcements
from .faq import FaqHandler
from .log import EventLogger
from .moderation import Moderator


class BotApp:
    def __init__(self, config):
        self.config = config
        self.logger = EventLogger(config["logging"]["file"])
        self.moderator = Moderator(config["moderation"], self.logger)
        self.faq = FaqHandler(config["faq"], self.logger)
        self.announce = Announcements(config["announce"], self.logger)
        self._last_highlight = None

    def build(self):
        app = Application.builder().token(self._token()).build()
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.on_message))
        app.add_handler(CommandHandler("start", self.cmd_start))
        app.add_handler(CommandHandler("help", self.cmd_help))
        app.add_handler(CommandHandler("announce", self.cmd_announce))
        app.add_handler(CommandHandler("ban", self.cmd_ban))
        app.add_handler(CommandHandler("unban", self.cmd_unban))
        app.add_handler(CommandHandler("stats", self.cmd_stats))
        return app

    def _token(self):
        return self.config["bot_token"]

    async def on_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.effective_message
        if msg is None or msg.from_user is None or msg.text is None:
            return
        chat_id = msg.chat_id
        user = msg.from_user
        self.logger.log(
            "message",
            {"chat": chat_id, "user": user.id, "username": user.username, "length": len(msg.text)},
        )
        verdict = self.moderator.check_message(chat_id, user.id, msg.text)
        if verdict == "ban":
            await msg.delete()
            await msg.chat.ban_member(user.id)
            self.logger.log("ban", {"chat": chat_id, "user": user.id})
            await context.bot.send_message(
                chat_id,
                f"@{user.username or user.id} fue bloqueado por violar las reglas del grupo.",
            )
            return
        if verdict != "ok":
            await msg.delete()
            self.logger.log("warn", {"chat": chat_id, "user": user.id, "reason": verdict})
            if not self.moderator.recently_warned(user.id):
                self.moderator.mark_warned(user.id)
                await context.bot.send_message(
                    chat_id,
                    f"@{user.username or user.id}: tu mensaje fue eliminado por infringir las reglas. "
                    f"Tercera infracción = bloqueo.",
                )
            return
        answer = self.faq.answer(msg.text)
        if answer and self.config["faq"]["enabled"]:
            await context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            await msg.reply_text(answer)
            self.logger.log("faq_reply", {"chat": chat_id, "user": user.id})

    async def cmd_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.effective_message.reply_text(
            "nullforge — moderador de comunidades web3.\n"
            "Filtro spam automático, FAQ y anuncios de los admins.\n"
            "Usá /help para las opciones."
        )

    async def cmd_help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.effective_message.reply_text(
            "/start — presentación\n/help — esta ayuda\n"
            "Admins: /announce <texto> — anuncio destacado\n"
            "/ban <reply> — bloquear\n/unban <reply> — desbloquear\n"
            "/stats — actividad del grupo"
        )

    async def cmd_announce(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = update.effective_message
        if msg is None or msg.from_user is None:
            return
        admin_ids = self.config.get("admin_ids", [])
        text = msg.text.removeprefix("/announce").strip()
        prepared = self.announce.prepare(msg.from_user.id, admin_ids, text)
        if prepared is None:
            return
        await msg.reply_text(f"📢 {prepared}")
        self._last_highlight = prepared

    async def cmd_ban(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self._is_admin(update):
            return
        msg = update.effective_message
        target = msg.reply_to_message.from_user if msg and msg.reply_to_message else None
        if target is None:
            await msg.reply_text("Respondé al mensaje del usuario a bloquear.")
            return
        await msg.chat.ban_member(target.id)
        await msg.reply_text(f"@{target.username or target.id} fue bloqueado.")
        self.logger.log("manual_ban", {"chat": msg.chat_id, "user": target.id, "by": msg.from_user.id})

    async def cmd_unban(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self._is_admin(update):
            return
        msg = update.effective_message
        target = msg.reply_to_message.from_user if msg and msg.reply_to_message else None
        if target is None:
            await msg.reply_text("Respondé al mensaje del usuario a desbloquear.")
            return
        await msg.chat.unban_member(target.id)
        await msg.reply_text(f"@{target.username or target.id} fue desbloqueado.")
        self.logger.log("manual_unban", {"chat": msg.chat_id, "user": target.id, "by": msg.from_user.id})

    async def cmd_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not self._is_admin(update):
            return
        msg = update.effective_message
        await msg.reply_text(
            "Métricas del bot (memoria de sesión):\n"
            "Las estadísticas agregadas se listan en logs/events.jsonl."
        )

    def _is_admin(self, update: Update) -> bool:
        user = update.effective_message.from_user
        return user.id in self.config.get("admin_ids", [])

    async def run_polling(self):
        logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")
        app = self.build()
        await app.run_polling()