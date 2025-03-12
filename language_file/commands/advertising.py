translations = {
    "extension": {
        "ru": "📢 **Продвигайте свои проекты вместе с Мухамед Ads!**\n\n"
                "Хотите привлечь новых клиентов или рассказать о своем продукте? Мы предлагаем эффективные решения для продвижения ваших идей!\n\n"
                "📌 **Виды рекламы:**\n"
                "- **Посты с текстом и изображением** — классический формат для привлечения внимания.\n"
                "- **Видеовставки** — интеграция вашего продукта в видеоконтент.\n"
                "- **Создание рекламных роликов** — профессиональный монтаж и креативный подход.\n"
                "- **Закрепленные посты** — максимальная видимость для вашего сообщения.\n\n"
                "🎯 **Мы предлагаем размещение рекламы на следующих популярных проектах:**\n"
                "- **Game Quest** — всё о видеоиграх и игровой индустрии.\n"
                "- **Nanson** — канал про классную и современную музыку без ап.\n"
                "- **ANIME INDUSTRY** — мир подборок новинок аниме и обзоры.\n"
                "- **KINO INDUSTRY** — кинообзоры, новинки кино, сериалов и мультфильмов.\n"
                "- **Стримус** — платформа для любителей стримов и развлечений.\n\n"
                "🌐 **Узнайте больше:**\n"
                "Подробности о наших услугах, условиях сотрудничества и актуальных возможностях для каждого проекта вы можете найти на нашем [сайте](https://muhamedlabs.pro)",

        "en": "📢 **Promote your projects with Muhamed Ads!**\n\n"
                "Want to attract new clients or tell the world about your product? We offer effective solutions to promote your ideas!\n\n"
                "📌 **Types of advertising:**\n"
                "- **Text and image posts** — a classic format to grab attention.\n"
                "- **Video integrations** — seamless inclusion of your product in video content.\n"
                "- **Creation of promotional videos** — professional editing and creative approach.\n"
                "- **Pinned posts** — maximum visibility for your message.\n\n"
                "🎯 **We offer advertising placement on the following popular projects:**\n"
                "- **Game Quest** — everything about video games and the gaming industry.\n"
                "- **Nanson** — a channel about cool and modern music without limits.\n"
                "- **ANIME INDUSTRY** — the world of anime reviews and new releases.\n"
                "- **KINO INDUSTRY** — movie reviews, new films, series, and cartoons.\n"
                "- **Стримус** — a platform for stream lovers and entertainment.\n\n"
                "🌐 **Learn more:**\n"
                "Details about our services, cooperation terms, and current opportunities for each project can be found on our [website](https://muhamedlabs.pro)",

        "uk": "📢 **Просувайте свої проекти разом із Мухамед Ads!**\n\n"
                "Хочете залучити нових клієнтів або розповісти про свій продукт? Ми пропонуємо ефективні рішення для просування ваших ідей!\n\n"
                "📌 **Види реклами:**\n"
                "- **Пости з текстом та зображенням** — класичний формат для привернення уваги.\n"
                "- **Відеовставки** — інтеграція вашого продукту у відеоконтент.\n"
                "- **Створення рекламних роликів** — професійний монтаж та креативний підхід.\n"
                "- **Закріплені пости** — максимальна видимість для вашого повідомлення.\n\n"
                "🎯 **Ми пропонуємо розміщення реклами на наступних популярних проектах:**\n"
                "- **Game Quest** — все про відеоігри та ігрову індустрію.\n"
                "- **Nanson** — канал про круту та сучасну музику без обмежень.\n"
                "- **ANIME INDUSTRY** — світ оглядів та новинок аніме.\n"
                "- **KINO INDUSTRY** — огляди фільмів, новинки кіно, серіалів та мультфільмів.\n"
                "- **Стримус** — платформа для любителів стрімів та розваг.\n\n"
                "🌐 **Дізнайтесь більше:**\n"
                "Деталі про наші послуги, умови співпраці та актуальні можливості для кожного проекту ви можете знайти на нашому [сайті](https://muhamedlabs.pro)"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский