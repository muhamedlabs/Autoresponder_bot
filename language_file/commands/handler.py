translations = {
    "unknown": {
        "ru": "📢 **Неизвестная команда**\n"
                "Проверьте полный список доступных команд сервиса:\n\n"
                "`!info` — Информация о создателе и многом другом.\n"
                "`!tyasitsu` — Уникальный чат для поклонников создателя.\n"
                "`!gift` — Специальные предложения для вас!\n"
                "`!news` — Новые обновления от Мухамеда.\n" 
                "`!start` — Перезапуск мини-бота user.\n"
                "`!advertising` — Узнать о наших рекламных услугах.\n"
                "`!donate` — Поддержите нас и помогите развивать проекты.\n"
                "`!faq` — Популярные вопросы и ответы.\n"
                "`!run` — Полный список доступных команд сервиса.\n"
                "`!quote` — Мудрые высказывания великих людей.\n"
                "`!picture` — Удивительные моменты от сервера Unsplash.\n"
                "`!podcast` — Запись идеи самого создателя.\n"
                "`!bots` — Все боты разработаны командой Muhamed IT Solutions.\n"
                "`!skeddy` — Планы, идеи и амбициозные цели Андрея Мухамеда.\n"
                "`/comment текст` — Написать отзыв о Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 Если вам нужна помощь, просто подождите, я скоро вам напишу!",

        "en": "📢 **Unknown command**\n"
                "Check the full list of available service commands:\n\n"
                "`!info` — Information about the creator and much more.\n"
                "`!tyasitsu` — A unique chat room for fans of the creator.\n"
                "`!gift` — Special offers for you!\n"
                "`!news` — New updates from Mohamed.\n"
                "`!start` — Re-launching the mini-bot user.\n"
                "`!advertising` — Learn about our advertising services.\n"
                "`!donate` — Support us and help us develop our projects.\n"
                "`!faq` — Popular questions and answers.\n"
                "`!run` — Full list of available service commands.\n"
                "`!quote` — Wise sayings of great men.\n"
                "`!picture` — Amazing moments from the Unsplash server.\n"
                "`!podcast` — A recording of the creator's own ideas.\n"
                "`!bots` — All bots are designed by Muhamed IT Solutions.\n"
                "`!skeddy` — Plans, ideas and ambitious goals of Andrew Muhamed.\n"
                "`/comment text` — Write a review about Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 If you need help, just wait, I'll write to you soon!",

        "uk": "📢 **Невідома команда**\n"
                "Перевірте повний список доступних команд сервісу:\n\n"
                "`!info` — Інформація про творця та багато іншого.\n"
                "`!tyasitsu` — Унікальний чат для шанувальників творця.\n"
                "`!gift` — Спеціальні пропозиції для вас!\n"
                "`!news` — Нові оновлення від Мухамеда.\n"
                "`!start` — Перезапуск міні-бота user.\n"
                "`!advertising` — Дізнатися про наші рекламні послуги.\n"
                "`!donate` — Підтримайте нас і допоможіть розвивати проекти.\n"
                "`!faq` — Популярні питання та відповіді.\n"
                "`!run` — Повний список доступних команд сервісу.\n"
                "`!quote` — Мудрі вислови великих людей.\n"
                "`!picture` — Дивовижні моменти з сервера Unsplash.\n"
                "`!podcast` — Запис ідей самого творця.\n"
                "`!bots` — Усі боти розроблені командою Muhamed IT Solutions.\n"
                "`!skeddy` — Плани, ідеї та амбітні цілі Андрея Мухамеда.\n"
                "`/comment текст` — Написати відгук про Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 Якщо вам потрібна допомога, просто зачекайте, я скоро вам напишу!"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский