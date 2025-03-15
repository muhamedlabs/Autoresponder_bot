import random

translations = {
    "comment_response": {
        "ru": [
            "✅ **Ваш комментарий успешно сохранён!**\n\n"
            "Спасибо, что поделились своими мытслями! 💭 Мы бережно сохранили их, чтобы однажды они стали частью нашей истории. Оставайтесь с нами — впереди ещё много интересного! 🚀💖",  

            "✨ **Ваш голос услышан!**\n\n"
            "Спасибо за ваш комментарий! Мы добавили его в нашу коллекцию идей. Кто знает, может, именно ваши слова вдохновят кого-то на что-то великое! 💡💫",  

            "🌟 **Комментарий сохранён!**\n\n"
            "Ваши мысли теперь часть нашего архива. Когда-нибудь они появятся на сайте, чтобы вдохновлять других. Спасибо, что делаете нас лучше! 💌",  

            "💾 **Ваш комментарий записан!**\n\n"
            "Мы сохранили ваши слова в нашем цифровом хранилище. Возможно, именно они станут началом чего-то грандиозного! Спасибо за ваш вклад! 🚀",  

            "📜 **Ваш комментарий в истории!**\n\n"
            "Спасибо, что оставили свой след! Мы сохранили ваши слова, и однажды они станут частью нашей истории. Оставайтесь с нами! 💖"
        ],
        "uk": [
            "✅ **Ваш коментар успішно збережено!**\n\n"
            "Дякуємо, що поділилися своїми думками! 💭 Ми бережно зберегли їх, щоб одного дня вони стали частиною нашої історії. Залишайтеся з нами — попереду ще багато цікавого! 🚀💖",  

            "✨ **Ваш голос почуто!**\n\n"
            "Дякуємо за ваш коментар! Ми додали його до нашої колекції ідей. Хто знає, можливо, саме ваші слова надихнуть когось на щось велике! 💡💫",  

            "🌟 **Коментар збережено!**\n\n"
            "Ваші думки тепер частина нашого архіву. Одного дня вони з'являться на сайті, щоб надихати інших. Дякуємо, що робите нас кращими! 💌",  

            "💾 **Ваш коментар записано!**\n\n"
            "Ми зберегли ваші слова в нашому цифровому сховищі. Можливо, саме вони стануть початком чогось грандіозного! Дякуємо за ваш внесок! 🚀",  

            "📜 **Ваш коментар у історії!**\n\n"
            "Дякуємо, що залишили свій слід! Ми зберегли ваші слова, і одного дня вони стануть частиною нашої історії. Залишайтеся з нами! 💖"
        ],
        "en": [
            "✅ **Your comment has been successfully saved!**\n\n"
            "Thank you for sharing your thoughts! 💭 We've carefully preserved them so that one day they can become part of our story. Stay with us — there's still so much exciting stuff ahead! 🚀💖",  

            "✨ **Your voice has been heard!**\n\n"
            "Thank you for your comment! We've added it to our collection of ideas. Who knows, maybe your words will inspire someone to do something great! 💡💫",  

            "🌟 **Comment saved!**\n\n"
            "Your thoughts are now part of our archive. Someday they'll appear on the website to inspire others. Thank you for making us better! 💌",  

            "💾 **Your comment has been recorded!**\n\n"
            "We've saved your words in our digital vault. Perhaps they'll be the start of something grand! Thank you for your contribution! 🚀",  

            "📜 **Your comment is now history!**\n\n"
            "Thank you for leaving your mark! We've saved your words, and one day they'll become part of our story. Stay with us! 💖"
        ]
    }
}

def get_translation(key, lang="ru"):
    """Возвращает случайный перевод по ключу."""
    translations_list = translations.get(key, {}).get(lang, translations[key]["ru"])
    return random.choice(translations_list) if isinstance(translations_list, list) else translations_list