"""Wiring del bot: handlers de telegram y orquestacion de modulos."""

from __future__ import annotations

import datetime

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from .announce import cmd_announce
from .faq import FaqEngine
from .log import EventLogger
from .moderation import Moderator


def build_app(cfg: dict) -> Application:
    app = Application.builder().token(cfg["bot_token"]).build()

    admin_ids: list[int] = cfg.get("admin_ids", [])
    moderator = Moderator(cfg.get("moderation", {}))
    faq = FaqEngine(cfg.get("faq", {}))
    logger = EventLogger(cfg.get("logging", {}).get("file", "logs/events.jsonl"))

    async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        msg = update.message
        if msg is None or msg.from_user is None or msg.from_user.is_bot:
            return
        user = msg.from_user
        text = (msg.text or msg.caption or "").strip()
        is_admin = user.id in admin_ids

        verdict = moderator.check(user.id, text, is_admin)
        if verdict.is_spam:
            await _apply_action(update, context, moderator, verdict.reason)
            logger.log("moderation", user_id=user.id, reason=verdict.reason)
            return

        if faq.enabled and text.endswith("?"):
            answer = faq.answer(text)
            if answer:
                await msg.reply_text(answer)
                logger.log("faq", user_id=user.id, question=text[:200])

    async def _apply_action(update: Update, context: ContextTypes.DEFAULT_TYPE,
                            mod: Moderator, reason: str) -> None:
        msg = update.message
        user = msg.from_user
        chat = msg.chat
        try:
            await msg.delete()
        except Exception:
            pass

        action = cfg.get("moderation", {}).get("action", "delete_and_warn")
        if action == "mute":
            until = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
                minutes=cfg.get("moderation", {}).get("mute_minutes", 60)
            )
            perms = {"can_send_messages": False}
            await context.bot.restrict_chat_member(
                chat.id, user.id, permissions=perms, until_date=until
            )
        elif action == "ban":
            await context.bot.ban_chat_member(chat.id, user.id)
        else:  # delete_and_warn
            total, ban = mod.add_warn(user.id)
            await chat.send_message(
                f"{user.mention_html()} — mensaje eliminado ({reason}). "
                f"Advertencia {total}.",
                parse_mode="HTML",
            )
            if ban:
                await context.bot.ban_chat_member(chat.id, user.id)
                logger.log("ban", user_id=user.id, warns=total)

    async def announce_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        await cmd_announce(update, context, admin_ids)

    async def faq_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Comando /preguntar <texto> — fuerza consulta al FAQ."""
        text = " ".join(context.args).strip()
        if not text:
            await update.message.reply_text("Uso: /preguntar <tu pregunta>")
            return
        answer = faq.answer(text) or "No tengo esa respuesta; un admin te va a ayudar."
        await update.message.reply_text(answer)

    app.add_handler(CommandHandler("announce", announce_handler))
    app.add_handler(CommandHandler("preguntar", faq_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    return app
