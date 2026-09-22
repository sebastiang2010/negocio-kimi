"""Anuncios de admins al grupo."""

from telegram import Update
from telegram.ext import ContextTypes


async def cmd_announce(update: Update, context: ContextTypes.DEFAULT_TYPE,
                       admin_ids: list[int]) -> None:
    """Uso: /announce <texto> — solo admins definidos en config."""
    user = update.effective_user
    if user is None or user.id not in admin_ids:
        return
    text = " ".join(context.args).strip()
    if not text:
        await update.message.reply_text("Uso: /announce <texto>")
        return
    await update.effective_chat.send_message(f"ANUNCIO\n\n{text}")
