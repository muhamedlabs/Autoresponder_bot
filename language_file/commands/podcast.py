translations = {
    "no_podcast": {
        "ru": "🎙 **Подкасты временно в разработке!** \n\n" 
                "Мы усердно трудимся, чтобы создать для вас что-то по-настоящему крутое: захватывающие темы, эксклюзивные инсайты "
                "и мотивирующие истории, которые зарядят вас энергией. Скоро всё будет готово! \n\n" 
                "__P.S. Подписывайтесь на наш__ [Telegram-канал](https://t.me/muhamedlabs)__, чтобы первыми узнать о запуске!__ 😉",

        "en": "🎙 **Podcasts are temporarily in development!**\n\n"
                "We are working hard to create something truly awesome for you: exciting topics, exclusive insights, "
                "and inspiring stories that will energize you. Everything will be ready soon!\n\n"
                "__P.S. Subscribe to our__ [Telegram channel](https://t.me/muhamedlabs)__ to be the first to know about the launch!__ 😉",

        "uk": "🎙 **Подкасти тимчасово у розробці!**\n\n"
                "Ми наполегливо працюємо, щоб створити для вас щось дійсно круте: захопливі теми, ексклюзивні інсайти "
                "та надихаючі історії, які зарядять вас енергією. Скоро все буде готово!\n\n"
                "__P.S. Підписуйтесь на наш__ [Telegram-канал](https://t.me/muhamedlabs)__, щоб першими дізнатися про запуск!__ 😉"
    },

    "is_podcast": {
        "ru": "🎙 **Подкаст, который вы ждали, уже здесь!** \n\n"
                "Готовьтесь к увлекательному путешествию: грандиозные цели, истории, которые вдохновляют, и эксклюзивные "
                "подробности о наших проектах. Время зажечь новые идеи!\n\n"  
                "__P.S. Переводчик в отпуске, так что подкаст только на русском. Зато с душой!__ 😌",

        "en": "🎙 **The podcast you've been waiting for is here!**\n\n"
                "Get ready for an exciting journey: big goals, inspiring stories, and exclusive "
                "details about our projects. It's time to ignite new ideas!\n\n"
                "__P.S. The translator is on vacation, so the podcast is only in Russian. But it's made with soul!__ 😌",

        "uk": "🎙 **Подкаст, якого ви чекали, уже тут!**\n\n"
                "Готуйтеся до захоплюючої подорожі: грандіозні цілі, надихаючі історії та ексклюзивні "
                "подробиці про наші проекти. Час запалити нові ідеї!\n\n"
                "__P.S. Перекладач у відпустці, тому подкаст лише російською. Зате з душею!__ 😌"
    }

}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский