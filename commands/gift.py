async def handle_gift(client, chat_id):
    await client.send_message(
        chat_id,
        "🎁 **Подарок от Андрея Мухамеда!** 🎁\n\n"
        "Пока ты ждёшь ответ от **Андрея Мухамеда**, мы приготовили для тебя небольшой, но приятный сюрприз! 😎\n\n"
        "Внутри ты найдёшь:\n"
        "✅ Авторские работы\n"
        "✅ Файлы для **After Effects**, **Blender**, **Premiere** и **Photoshop**\n\n"
        "Не упусти шанс получить этот подарок! 🎉 "
        "Получай свой подарок по ссылке ниже:\n\n"
        "🔗 [Скачать подарок](https://bit.ly/4hY2kmK)\n\n",
        file="Фото_материал/2 copy.png"  # Укажите путь к файлу изображения
    )

