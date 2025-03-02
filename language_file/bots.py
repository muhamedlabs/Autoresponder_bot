translations = {
    "programs": {
        "ru": "🤖 **Muhamed IT Solutions** — команда профессионалов, специализирующаяся на создании инновационных решений в области IT. 🚀\n\n"
                "Мы занимаемся разработкой ботов, автоматизацией процессов и цифровым маркетингом.\n\n"
                "🛠️ Наши ключевые боты:\n"
                "1️⃣ [Project Manager](https://t.me/ProManagerss_bot) — Управление проектами и задачами.\n"
                "2️⃣ [Game Quest](https://t.me/GQ_newsbot) — Новости и обновления мира игр.\n"
                "3️⃣ [Nanson](https://t.me/Nanson_CFNbot) — Помощь в обучении и карьерном росте.\n"
                "4️⃣ [Kinani Family](https://t.me/KinaniFamily_bot) — Общение и поддержка для всей семьи.\n\n"
                "🎮 **Discord боты** — У нас есть несколько Discord ботов, но они доступны на разных проектах.\n\n"
                "Присоединяйтесь к нашим ботам и узнайте, как они могут улучшить ваши процессы! 🌟",

        "en": "🤖 **Muhamed IT Solutions** — a team of professionals specializing in creating innovative IT solutions. 🚀\n\n"
                "We are engaged in bot development, process automation, and digital marketing.\n\n"
                "🛠️ Our key bots:\n"
                "1️⃣ [Project Manager](https://t.me/ProManagerss_bot) — Project and task management.\n"
                "2️⃣ [Game Quest](https://t.me/GQ_newsbot) — News and updates from the gaming world.\n"
                "3️⃣ [Nanson](https://t.me/Nanson_CFNbot) — Assistance in learning and career growth.\n"
                "4️⃣ [Kinani Family](https://t.me/KinaniFamily_bot) — Communication and support for the whole family.\n\n"
                "🎮 **Discord bots** — We have several Discord bots, but they are available on different projects.\n\n"
                "Join our bots and discover how they can improve your processes! 🌟",

        "uk": "🤖 **Muhamed IT Solutions** — команда професіоналів, яка спеціалізується на створенні інноваційних IT-рішень. 🚀\n\n"
                "Ми займаємося розробкою ботів, автоматизацією процесів та цифровим маркетингом.\n\n"
                "🛠️ Наші ключові боти:\n"
                "1️⃣ [Project Manager](https://t.me/ProManagerss_bot) — Управління проектами та завданнями.\n"
                "2️⃣ [Game Quest](https://t.me/GQ_newsbot) — Новини та оновлення зі світу ігор.\n"
                "3️⃣ [Nanson](https://t.me/Nanson_CFNbot) — Допомога у навчанні та кар’єрному зростанні.\n"
                "4️⃣ [Kinani Family](https://t.me/KinaniFamily_bot) — Спілкування та підтримка для всієї родини.\n\n"
                "🎮 **Discord боти** — У нас є кілька Discord ботів, але вони доступні на різних проектах.\n\n"
                "Приєднуйтесь до наших ботів і дізнайтеся, як вони можуть покращити ваші процеси! 🌟"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский