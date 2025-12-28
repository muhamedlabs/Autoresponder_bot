import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from BANNED_FILES.config import telegram_bots

user_started = set()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_started.add(user_id)
    await update.message.reply_text(
        "🚀 Чтобы увидеть полный функционал, просто напишите сообщения:\n"
        "https://t.me/admirall_times"
    )

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in user_started:
        await update.message.reply_text(
            "👀 Посмотрите сообщения в закроме, а пока подписывайтесь на канал создателя."
        )

async def start_mini_bot():
    """Запуск мини-бота полностью асинхронно в одном asyncio-цикле"""
    app = ApplicationBuilder().token(telegram_bots).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.PRIVATE, handle_messages))

    await app.initialize()       # Инициализация приложения
    await app.start()            # Старт бота
    print("MiniBot Started async")

    # Запуск polling без блокировки
    asyncio.create_task(app.updater.start_polling())

    # Бесконечная задержка, чтобы задача не завершилась
    while True:
        await asyncio.sleep(3600)

