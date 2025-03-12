translations = {
    "correspondence": {
        "ru": "📢 **Добро пожаловать в Топ чат Тясицу!**\n\n"
                "Ты попал в место, где каждый найдет что-то для себя! Здесь ты можешь не только приятно пообщаться, но и узнать много интересного — "
                "получить полезные советы, обсудить новинки, найти единомышленников и просто провести время в компании хороших людей. 🌟\n\n"
                "Наш чат — это не просто место для общения, это целая комьюнити, где каждый участник важен. "
                "Мы всегда рады новым друзьям, и у нас всегда есть чем поделиться.\n\n"
                "Помимо этого, в чате тебя ждут регулярные обсуждения интересных тем, конкурсы, а также множество других активностей, "
                "которые сделают твое пребывание незабываемым.\n\n"
                "Так что не теряй времени и присоединяйся прямо сейчас! Нам есть о чём поговорить! 😉\n\n"
                "👉 [Залетай в чат Тясицу и становись частью нашей команды!](https://t.me/+QxnWNDp95wFhOWFi)",

        "en": "📢 **Welcome to the Top Tyasitsu Chat!**\n\n"
                "You've found a place where everyone can find something for themselves! Here, you can not only have a pleasant conversation but also learn a lot of interesting things — "
                "get useful advice, discuss new releases, find like-minded people, and simply spend time in the company of good people. 🌟\n\n"
                "Our chat is not just a place for communication; it's a whole community where every member matters. "
                "We are always happy to welcome new friends, and we always have something to share.\n\n"
                "In addition, the chat offers regular discussions on interesting topics, contests, and many other activities "
                "that will make your stay unforgettable.\n\n"
                "So don't waste any time and join right now! We have a lot to talk about! 😉\n\n"
                "👉 [Join the Tyasitsu chat and become part of our team!](https://t.me/+QxnWNDp95wFhOWFi)",

        "uk": "📢 **Ласкаво просимо до Топ чату Тясицю!**\n\n"
                "Ти потрапив у місце, де кожен знайде щось для себе! Тут ти можеш не лише приємно поспілкуватися, а й дізнатися багато цікавого — "
                "отримати корисні поради, обговорити новинки, знайти однодумців і просто провести час у компанії хороших людей. 🌟\n\n"
                "Наш чат — це не просто місце для спілкування, це ціла спільнота, де кожен учасник важливий. "
                "Ми завжди раді новим друзям, і у нас завжди є чим поділитися.\n\n"
                "Крім того, у чаті тебе чекають регулярні обговорення цікавих тем, конкурси, а також безліч інших активностей, "
                "які зроблять твій час тут незабутнім.\n\n"
                "Тож не гаяй часу і приєднуйся прямо зараз! Нам є про що поговорити! 😉\n\n"
                "👉 [Залітай у чат Тясицю та ставай частиною нашої команди!](https://t.me/+QxnWNDp95wFhOWFi)"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский