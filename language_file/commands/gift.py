translations = {
    "grant": {
        "ru": "🎁 **Подарок от Андрея Мухамеда!** 🎁\n\n"
                "Пока ты ждёшь ответ от **Андрея Мухамеда**, мы приготовили для тебя небольшой, но приятный сюрприз! 😎\n\n"
                "Внутри ты найдёшь:\n"
                "✅ Авторские работы\n"
                "✅ Файлы для **After Effects**, **Blender**, **Premiere** и **Photoshop**\n\n"
                "Не упусти шанс получить этот подарок! 🎉 "
                "Получай свой подарок по ссылке ниже:\n\n"
                "🔗 [Скачать подарок](https://bit.ly/4hY2kmK)\n\n",

        "en": "🎁 **A Gift from Andrey Muhamed!** 🎁\n\n"
                "While you're waiting for a response from **Andrey Muhamed**, we've prepared a small but pleasant surprise for you! 😎\n\n"
                "Inside, you'll find:\n"
                "✅ Original works\n"
                "✅ Files for **After Effects**, **Blender**, **Premiere**, and **Photoshop**\n\n"
                "Don't miss the chance to receive this gift! 🎉 "
                "Get your gift using the link below:\n\n"
                "🔗 [Download the gift](https://bit.ly/4hY2kmK)\n\n",

        "uk": "🎁 **Подарунок від Андрея Мухамеда!** 🎁\n\n"
                "Поки ти чекаєш на відповідь від **Андрея Мухамеда**, ми приготували для тебе невеликий, але приємний сюрприз! 😎\n\n"
                "Усередині ти знайдеш:\n"
                "✅ Авторські роботи\n"
                "✅ Файли для **After Effects**, **Blender**, **Premiere** та **Photoshop**\n\n"
                "Не пропусти можливість отримати цей подарунок! 🎉 "
                "Отримай свій подарунок за посиланням нижче:\n\n"
                "🔗 [Завантажити подарунок](https://bit.ly/4hY2kmK)\n\n"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский