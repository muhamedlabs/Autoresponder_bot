import asyncio
import os
import random
import re
from telethon import events

# Рандомные рабочие сообщения
RESPONSES = [  
    "**Держись, БРО!** 💪\n\nРабота — это твой путь к успеху! Вкладывай усилия, двигайся вперёд, и результат не заставит себя ждать! 🚀🔥",  

    "**БРО, давай покажем этому миру, на что ты способен!** 💼\n\nУ тебя есть все шансы сделать этот день продуктивным и максимально эффективным! Дерзай! 💪",  

    "**Рабочий режим активирован, БРО!** 🎯\n\nПусть задачи выполняются легко, идеи приходят быстро, а результат радует! Ты справишься, не сомневаюсь! 🚀",  

    "**Фокус на цели, БРО!** 🎯\n\nНе отвлекайся на мелочи, двигайся вперёд и покажи всем, кто тут босс! Успех ждёт, осталось только взять его! 🔥",  

    "**Настало время покорять новые вершины, БРО!** 🏆\n\nРабота — это не просто рутина, а шаг к твоим мечтам. Включайся в процесс и добивайся результатов! 🚀",  

    "**Работаем, БРО!** ⏳\n\nКаждое действие приближает тебя к успеху, так что выкладывайся на максимум! Главное — двигаться вперёд и верить в себя! 🔥",  

    "**Продуктивность на максимум, БРО!** 💡\n\nПусть работа спорится, задачи решаются, а день принесёт крутейшие результаты! Всё в твоих руках! 💪",  

    "**Заряжайся, БРО!** ⚡️\n\nПусть этот день будет мега-продуктивным! Вкладывай энергию в дело, и оно обязательно принесёт крутые плоды! 🚀🔥",  

    "**БРО, работа — это твоя арена, а ты — победитель!** 🏆\n\nНе останавливайся, пробивайся к своим целям и доказывай, что ты лучший! 💼💪",  

    "**Сегодня отличный день, чтобы сделать шаг к успеху, БРО!** 🚀\n\nВперёд, крутить мир в свою сторону, добиваться целей и оставлять свой след! 🔥",  
]  

# Рандомные комментарии к песне
SONG_COMMENTS = [  
    "Идеальный трек для продуктивного дня! 🎶💼",  

    "Работа идёт легче под такую музыку! 🚀🔥",  

    "Настроение на максимум, задачи решаются сами! 💪🎧",  

    "Этот трек заряжает на продуктивность! 💼⚡",  

    "Музыкальный допинг для рабочего процесса! 🔥🎵",  

    "С таким саундтреком работа — одно удовольствие! 🎶💪",  

    "Плейлист для продуктивности пополнился! 🎧💼",  

    "Энергия +100%! Готов покорять рабочие вершины! 🚀",  

    "Этот бит помогает сосредоточиться! 🎵🎯",  

    "Музыка, которая мотивирует работать усерднее! 💡🔥",  
]  

# Пути к папкам
IMAGE_FOLDER = os.path.abspath("Фото_материал/Photo_design/Alex_Diaconu_РАБОТА")  # Папка с картинками
MUSIC_FOLDER = os.path.abspath("Подкаст_музика/Music_designer/Nanson_РАБОТА")  # Папка с песнями

def register_auto_reply(client):
    """Регистрирует автоответ на **точное написание** 'РаботаPro'."""
    
    @client.on(events.NewMessage(outgoing=True))
    async def auto_reply(event):
        # Проверяем точное написание "РаботаPro"
        if re.fullmatch(r"РаботаPro", event.message.text):  
            await asyncio.sleep(1)

            random_text = random.choice(RESPONSES)

            # Проверяем наличие папки с картинками
            if not os.path.exists(IMAGE_FOLDER):
                print(f"Ошибка: Папка '{IMAGE_FOLDER}' не найдена!")
                await event.respond(random_text)
                return

            images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

            if images:
                random_image = os.path.join(IMAGE_FOLDER, random.choice(images))
                await event.client.send_file(event.chat_id, random_image, caption=random_text)
                print(f"Reply to 'WorkPro' with picture")
            else:
                await event.respond(random_text)
                print(f"Ответ без картинки (нет файлов в папке)")

            # Задержка 2 минуты 30 секунд перед отправкой музыки
            await asyncio.sleep(150)  

            # Проверяем наличие папки с музыкой
            if not os.path.exists(MUSIC_FOLDER):
                print(f"Ошибка: Папка '{MUSIC_FOLDER}' не найдена!")
                return

            songs = [f for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith((".mp3", ".wav", ".ogg"))]

            if songs:
                random_song = os.path.join(MUSIC_FOLDER, random.choice(songs))
                random_comment = random.choice(SONG_COMMENTS)
                await event.client.send_file(event.chat_id, random_song, caption=random_comment)
                print(f"🎵 Track sent: {random_song}")
            else:
                print("Ошибка: В папке с музыкой нет файлов!")