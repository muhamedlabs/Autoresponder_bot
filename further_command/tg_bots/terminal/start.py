from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

user_started = set()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_started.add(user_id)
    await update.message.reply_text(
        "🚀 Чтобы увидеть полный функционал, просто напишите сообщения:\n"
        "https://t.me/admirall_times"
    )

def command_handler():
    """Возвращает обработчик команды /start"""
    return CommandHandler("start", start_command)