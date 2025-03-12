translations = {
    "ru": {
        "image_caption": "🌍 **Яркие моменты от Unsplash**\n\n"
                         "Смотреть изображение: [тут]({image_url})\n\n"
                         "Автор: [{author}]({author_url})\n\n"
                         "Описание: {description}\n\n",
        "error_message": "❌ **Ошибка при загрузке изображения**\n\n"
                         "К сожалению, сейчас мы не можем загрузить новое изображение. "
                         "Попробуйте снова через некоторое время.\n\n"
                         "Мы всегда стремимся радовать вас лучшими моментами!"
    },
    "en": {
        "image_caption": "🌍 **Highlights from Unsplash**\n\n"
                         "View image: [here]({image_url})\n\n"
                         "Author: [{author}]({author_url})\n\n"
                         "Description: {description}\n\n",
        "error_message": "❌ **Error loading image**\n\n"
                         "Unfortunately, we cannot load a new image right now. "
                         "Please try again later.\n\n"
                         "We always strive to bring you the best moments!"
    },
    "uk": {
        "image_caption": "🌍 **Яскраві моменти від Unsplash**\n\n"
                         "Переглянути зображення: [тут]({image_url})\n\n"
                         "Автор: [{author}]({author_url})\n\n"
                         "Опис: {description}\n\n",
        "error_message": "❌ **Помилка завантаження зображення**\n\n"
                         "На жаль, зараз ми не можемо завантажити нове зображення. "
                         "Спробуйте ще раз пізніше.\n\n"
                         "Ми завжди прагнемо радувати вас найкращими моментами!"
    }
}

def get_translation(key, lang="ru"):
    """Функция получения перевода по ключу и языку. Если ключа нет — возвращает предупреждение."""
    return translations.get(lang, translations["ru"]).get(key, f"⚠️ Перевод отсутствует: {key}")