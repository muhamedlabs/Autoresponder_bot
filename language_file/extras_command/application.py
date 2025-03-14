translations = {
    "biography_text": {
        "ru": [
            "**Андрей Мухамед — креативный предприниматель и вдохновитель инновационных проектов.**\n\n"
            "🌟 Его деятельность охватывает **рекламу, технологии и цифровой контент**, объединяя идеи и возможности, чтобы создавать нечто уникальное.\n\n"
            "**Владелец пяти динамично развивающихся каналов:**\n"
            "— 🎮 __Game Quest__ - всё о видеоиграх и их индустрии;\n"
            "— 🔥 __Nanson__ - актуальные песни без ап;\n"
            "— 🎌 __ANIME INDUSTRY__ - мир подборок новинок аниме;\n"
            "— 🎥 __KINO INDUSTRY__ - новинки кино, сериалов и мультфильмов;\n"
            "— 🎧 __Стримус__ - просто стримы от души.\n\n"
            "💻 Помимо этого, Андрей активно занимается **программированием, управлением соцсетями, рекламой, написанием сценариев, видеомонтажом и созданием контента**.\n\n"
            "**Его главная цель — вдохновлять и создавать что-то** [новое!](https://muhamedlabs.pro)"
        ],
        "uk": [
            "**Андрей Мухамед — креативний підприємець і натхненник інноваційних проектів.**\n\n"
            "🌟 Його діяльність охоплює **рекламу, технології та цифровий контент**, поєднуючи ідеї та можливості для створення чогось унікального.\n\n"
            "**Власник п'яти динамічно розвиваючихся каналів:**\n"
            "— 🎮 __Game Quest__ - все про відеоігри та їхню індустрію;\n"
            "— 🔥 __Nanson__ - актуальні пісні без ап;\n"
            "— 🎌 __ANIME INDUSTRY__ - світ підбірок новинок аніме;\n"
            "— 🎥 __KINO INDUSTRY__ - новинки кіно, серіалів та мультфільмів;\n"
            "— 🎧 __Стрімус__ - просто стріми від душі.\n\n"
            "💻 Крім того, Андрей активно займається **програмуванням, управлінням соцмережами, рекламою, написанням сценаріїв, відеомонтажем та створенням контенту**.\n\n"
            "**Його головна мета — надихати та створювати щось** [нове!](https://muhamedlabs.pro)"
        ],
        "en": [
            "**Andrey Muhamed is a creative entrepreneur and an inspirer of innovative projects.**\n\n"
            "🌟 His activities cover **advertising, technology, and digital content**, combining ideas and opportunities to create something unique.\n\n"
            "**Owner of five dynamically developing channels:**\n"
            "— 🎮 __Game Quest__ - everything about video games and their industry;\n"
            "— 🔥 __Nanson__ - trending songs without ads;\n"
            "— 🎌 __ANIME INDUSTRY__ - the world of anime new releases;\n"
            "— 🎥 __KINO INDUSTRY__ - new movies, series, and cartoons;\n"
            "— 🎧 __Strimus__ - just heartfelt streams.\n\n"
            "💻 In addition, Andrey is actively engaged in **programming, social media management, advertising, scriptwriting, video editing, and content creation**.\n\n"
            "**His main goal is to inspire and create something** [new!](https://muhamedlabs.pro)"
        ]
    }
}


def get_translation(key, lang):
    """Получает перевод на нужном языке, если нет — использует русский."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])