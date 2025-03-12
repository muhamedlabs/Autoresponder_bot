translations = {
    "money": {
        "ru": "💵 **Ваш вклад имеет огромное значение!**\n\n"
                "Ваша поддержка помогает нам продолжать создавать качественный контент и внедрять новые функции, чтобы радовать вас интересными и полезными материалами. 🎬\n\n"
                "Мы ценим вашу помощь и обещаем не останавливаться на достигнутом! 🙏\n\n"
                "💳 Присоединяйтесь к нам и поддержите наш проект через одну из платформ:\n"
                "🔹 [Donationalerts](https://www.donationalerts.com/r/andremuhamad) — Поддержите нас здесь! 💬\n"
                "🔹 [Patreon](https://www.patreon.com/andremuhamad) — Подписывайтесь на эксклюзивный контент! 🎁\n\n"
                "Каждый вклад помогает нам двигаться дальше! Благодарим за вашу поддержку! 🌟",

        "en": "💵 **Your contribution matters greatly!**\n\n"
                "Your support helps us continue creating quality content and implementing new features to delight you with interesting and useful materials. 🎬\n\n"
                "We appreciate your help and promise not to stop at what we've achieved! 🙏\n\n"
                "💳 Join us and support our project through one of the platforms:\n"
                "🔹 [Donationalerts](https://www.donationalerts.com/r/andremuhamad) — Support us here! 💬\n"
                "🔹 [Patreon](https://www.patreon.com/andremuhamad) — Subscribe for exclusive content! 🎁\n\n"
                "Every contribution helps us move forward! Thank you for your support! 🌟",

        "uk": "💵 **Ваш внесок має величезне значення!**\n\n"
                "Ваша підтримка допомагає нам продовжувати створювати якісний контент та впроваджувати нові функції, щоб радувати вас цікавими та корисними матеріалами. 🎬\n\n"
                "Ми цінуємо вашу допомогу та обіцяємо не зупинятися на досягнутому! 🙏\n\n"
                "💳 Приєднуйтесь до нас та підтримайте наш проект через одну з платформ:\n"
                "🔹 [Donationalerts](https://www.donationalerts.com/r/andremuhamad) — Підтримайте нас тут! 💬\n"
                "🔹 [Patreon](https://www.patreon.com/andremuhamad) — Підписуйтесь на ексклюзивний контент! 🎁\n\n"
                "Кожен внесок допомагає нам рухатися вперед! Дякуємо за вашу підтримку! 🌟"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский