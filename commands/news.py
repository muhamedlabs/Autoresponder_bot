async def handle_news(client, chat_id):
    await client.send_message(
        chat_id,
        "📢 **Новости!**\n\n"
        "Мы активно развиваемся во всех сферах, но самое главное — "
        "мы работаем над созданием **обственного хостинга**! 🚀\n\n"
        "Чтобы быть в курсе всех обновлений и подробностей, "
        "подписывайтесь на наш [Telegram-канал!](https://t.me/muhamedlabs)",
        file="Видео_материал/Сайт.mp4"  # Укажите путь к вашему видео
    )
