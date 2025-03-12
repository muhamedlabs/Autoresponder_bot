translations = {
    "television": {
        "ru": "**📢 Важное объявление!**\n\n" 
                "Мы не стоим на месте и активно движемся вперед во всех направлениях! Но главное — " 
                "мы работаем над созданием **собственного хостинга**, который станет настоящим прорывом!\n\n  "
                "Чтобы первыми узнавать обо всех обновлениях, новостях и эксклюзивных подробностях, "
                "подписывайтесь на наш [Telegram-канал.](https://t.me/muhamedlabs) \n\n__Не пропустите ничего важного!__ 💥 ",


        "en": "**📢 Important Announcement!**\n\n"
                "We are not standing still and are actively moving forward in all directions! But most importantly — "
                "we are working on creating **our own hosting**, which will be a real breakthrough!\n\n"
                "To be the first to know about all updates, news, and exclusive details, "
                "subscribe to our [Telegram channel.](https://t.me/muhamedlabs) \n\n__Don't miss anything important!__ 💥",

        "uk": "**📢 Важливе оголошення!**\n\n"
                "Ми не стоїмо на місці та активно рухаємося вперед у всіх напрямках! Але найголовніше — "
                "ми працюємо над створенням **власного хостингу**, який стане справжнім проривом! 🌟\n\n"
                "Щоб першими дізнаватися про всі оновлення, новини та ексклюзивні подробиці, "
                "підписуйтесь на наш [Telegram-канал.](https://t.me/muhamedlabs) \n\n__Не пропустіть нічого важливого!__ 💥"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский