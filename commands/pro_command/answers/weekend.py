import os
import random
from telethon import events

# Путь к гифке
GIF_PATH = os.path.abspath("Видео_материал/Gif/Resting.gif")

# Рандомные тексты для ответа
WEEKEND_MESSAGES = [  
    "**Наступил выходной! 🎉**\n\nВремя расслабиться, отдохнуть и перезарядиться! Наслаждайся моментом и не забывай про веселье! 😎🔥",  

    "**Выходной, БРО! 🚀**\n\nЗабудь про будничные заботы, сегодня только кайф и отдых! Пусть этот день принесёт кучу позитива! 🎊",  

    "**День отдыха активирован! ☀️**\n\nПора выключить рабочий режим и включить режим чилла! Наслаждайся выходным! 🏖️",  

    "**Время чилла! 🎶**\n\nСегодня идеальный день для того, чтобы делать только то, что приносит удовольствие! Пусть выходной пройдёт на 100%! 🍹",  

    "**Выходной — это святое! 🙌**\n\nОтдыхай, заряжайся энергией и наслаждайся каждым моментом! Удачного дня! 😍",  
]  

def register_auto_reply(client):
    """Регистрирует автоответ на слово 'виходной'."""

    @client.on(events.NewMessage(outgoing=True))
    async def weekend_reply(event):
        if "виходной" in event.message.text.lower():
            # Проверяем, что сообщение в личке
            if event.is_group or event.is_channel:
                return  # В группах не реагируем

            random_text = random.choice(WEEKEND_MESSAGES)

            if not os.path.exists(GIF_PATH):
                print(f"Ошибка: Файл гифки '{GIF_PATH}' не найден!")
                await event.respond(random_text)
                return

            await event.client.send_file(event.chat_id, GIF_PATH, caption=random_text)
            print(f"Sent a gif with a text for the weekend.")
