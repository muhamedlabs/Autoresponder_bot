translations = {
    "image_caption": {
        "ru": "ЕСЛИ Я В ОНЛАЙНЕ И НЕ ОТВЕЧАЮ НА ВАШИ СООБЩЕНИЯ, ЭТО ЗНАЧИТ ЧТО ЦАРЬ СЕЙЧАС СЛУШАЕТ МУЗЫКУ 🎶👑",
        "uk": "ЯКЩО Я В ОНЛАЙНІ І НЕ ВІДПОВІДАЮ НА ВАШІ ПОВІДОМЛЕННЯ, ЦЕ ОЗНАЧАЄ ЩО ЦАР ЗАРАЗ СЛУХАЄ МУЗИКУ 🎶👑",
        "en": "IF I AM ONLINE BUT NOT REPLYING, IT MEANS THE KING IS LISTENING TO MUSIC 🎶👑"
    },
    "song_comments": {
        "ru": [
            "Этот трек идеально подходит для отдыха... 😌🎶",
            "Наслаждайся этой атмосферной музыкой! 🌌✨",
            "Мелодия, которая унесёт тебя в мир грёз... 🎶💫",
            "Звуки, которые создают магию момента... ✨🎵",
            "Закрой глаза и погрузись в музыку... 🎧💙",
        ],
        "uk": [
            "Цей трек ідеально підходить для відпочинку... 😌🎶",
            "Насолоджуйся цією атмосферною музикою! 🌌✨",
            "Мелодія, яка перенесе тебе у світ мрій... 🎶💫",
            "Звуки, що створюють магію моменту... ✨🎵",
            "Заплющ очі та занурся в музику... 🎧💙",
        ],
        "en": [
            "This track is perfect for relaxation... 😌🎶",
            "Enjoy this atmospheric music! 🌌✨",
            "A melody that takes you to the world of dreams... 🎶💫",
            "Sounds that create a magical moment... ✨🎵",
            "Close your eyes and dive into the music... 🎧💙",
        ],
    }
}

def get_translation(key, lang):
    """Получает перевод на нужном языке, если нет — использует русский."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])
