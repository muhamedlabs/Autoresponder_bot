from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Доступные команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Получить справку\n"
        "/echo [текст] - Повторить текст"
    )

def command_handler():
    """Возвращает обработчик команды /help"""
    return CommandHandler("help", help_command)