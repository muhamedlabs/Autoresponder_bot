translations = {
    "information": {
        "ru": "📢 **Андрей Мухамед** — креативный предприниматель и создатель инновационных проектов в сфере рекламы, технологий и цифрового контента. "
                "Он объединяет идеи и возможности, чтобы вдохновлять и создавать новое.\n\n"
                "**Основные команды для взаимодействия:**\n"
                "`!info` — Информацию о создателе и многом другом.\n"
                "`!tyasitsu` — Уникальный чат для поклонников создателя.\n"
                "`!advertising` — Узнайте о рекламе и ознакомьтесь с ценами.\n"
                "`!run` — Полный список доступных команд сервиса.\n"
                "`!faq` — Популярные вопросы и ответы.\n"
                "`!donate` — Поддержите нас и помогите развивать проекты.\n"
                "`!gift` — Специальные предложения для вас!\n"
                "`!bots` — Все боты разработаны командой Muhamed IT Solutions.\n"
                "`!skeddy` — Планы, идеи и амбициозные цели Андрея Мухамеда.\n"
                "`/comment текст` — Написать отзыв о Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 Для получения более подробной информации, просто подождите, я скоро вам напишу!",

        "en": "📢 **Andrey Muhamed** — a creative entrepreneur and creator of innovative projects in the fields of advertising, technology, and digital content. "
                "He brings together ideas and opportunities to inspire and create something new.\n\n"
                "**Main commands for interaction:**\n"
                "`!info` — Information about the creator and much more.\n"
                "`!tyasitsu` — A unique chat for fans of the creator.\n"
                "`!advertising` — Learn about advertising and check the prices.\n"
                "`!run` — Full list of available service commands.\n"
                "`!faq` — Popular questions and answers.\n"
                "`!donate` — Support us and help develop our projects.\n"
                "`!gift` — Special offers for you!\n"
                "`!bots` — All bots are developed by Muhamed IT Solutions.\n"
                "`!skeddy` — Plans, ideas, and ambitious goals of Andrey Muhamed.\n"
                "`/comment text` — Write a review about Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 For more details, just wait, I'll write to you soon!",

        "uk": "📢 **Андрей Мухамед** — креативний підприємець і творець інноваційних проектів у сфері реклами, технологій та цифрового контенту. "
                "Він поєднує ідеї та можливості, щоб надихати і створювати нове.\n\n"
                "**Основні команди для взаємодії:**\n"
                "`!info` — Інформація про творця та багато іншого.\n"
                "`!tyasitsu` — Унікальний чат для шанувальників творця.\n"
                "`!advertising` — Дізнатись про рекламу та переглянути ціни.\n"
                "`!run` — Повний список доступних команд сервісу.\n"
                "`!faq` — Популярні питання та відповіді.\n"
                "`!donate` — Підтримайте нас і допоможіть розвивати проекти.\n"
                "`!gift` — Спеціальні пропозиції для вас!\n"
                "`!bots` — Усі боти розроблені командою Muhamed IT Solutions.\n"
                "`!skeddy` — Плани, ідеї та амбітні цілі Андрея Мухамеда.\n"
                "`/comment текст` — Написати відгук про Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 Для отримання більш детальної інформації, просто зачекайте, я скоро вам напишу!"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский