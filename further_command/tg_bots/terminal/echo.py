from telegram import Update
from telegram.ext import ContextTypes

async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        text = ' '.join(context.args)
        await update.message.reply_text(f"📢 {text}")
    else:
        await update.message.reply_text("Пожалуйста, укажите текст: /echo [ваш текст]")
    
def command_handler():
    from telegram.ext import CommandHandler
    return CommandHandler("echo", echo_command)