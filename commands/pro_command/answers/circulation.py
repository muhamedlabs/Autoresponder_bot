import asyncio
import os
import random
import re
from telethon import events

# Файл со списком чатов
CHAT_FILE = "Ignore/Auto_users.txt"  # Файл с данными чатов
GIF_PATH = os.path.abspath("Видео_материал/Gif/My.gif")  # Единственная гифка для отправки

WIN_MESSAGES = [  
    "**Поздравляем тебя, Ронин! 🎉**\n\nТы выиграл эксклюзивную возможность бесплатно прорекламироваться на наших проектах! 🚀 У тебя есть 24 часа, чтобы откликнуться. Не упусти шанс! 💪\n\nКстати, не забудь посетить наш сайт: https://muhamedlabs.pro",  

    "**Ронин, ты победитель! 🏆**\n\nТвоя удача сегодня на высоте! 😎 Ты получаешь возможность бесплатной рекламы (видео или текстовой) на наших проектах! Ждём твой ответ в течение 24 часов! ⏳\n\nКстати, не забудь заглянуть на наш сайт: https://muhamedlabs.pro",  

    "**Внимание, Ронин! Ты выиграл! 💥**\n\nПоздравляем с победой в розыгрыше! 🎊 У тебя есть 24 часа, чтобы забрать свой приз — бесплатную рекламу на наших площадках! Пиши скорее! 🚀\n\nКстати, не забудь посетить наш сайт: https://muhamedlabs.pro",  

    "**Вот это везение, Ронин! 🔥**\n\nТы стал победителем и теперь можешь получить свою бесплатную рекламу! 🏅 Напиши нам в течение 24 часов, чтобы активировать приз! ⏳\n\nКстати, не забудь заглянуть на сайт: https://muhamedlabs.pro",  

    "**Ты в центре внимания, Ронин! 🏅**\n\nТвой выигрыш — бесплатная реклама на наших проектах! 💪 Не упусти возможность, у тебя 24 часа, чтобы откликнуться! 🚀\n\nКстати, не забудь посетить наш сайт: https://muhamedlabs.pro",  
]  

# Функция загрузки списка чатов из файла (извлекаем только ID чатов)
def load_chat_ids():
    if not os.path.exists(CHAT_FILE):
        print(f"Ошибка: Файл '{CHAT_FILE}' не найден!")
        return []
    
    with open(CHAT_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    chat_ids = re.findall(r"ID чата: (\d+)", content)  # Регулярка для поиска ID
    return list(map(int, chat_ids))  # Преобразуем в список чисел

async def send_winner_messages(client):
    """Отправляет сообщение о выигрыше в 3 случайных чата."""
    chat_ids = load_chat_ids()
    
    if not chat_ids:
        print("Ошибка: Список чатов пуст!")
        return

    if len(chat_ids) < 3:
        print("Ошибка: В списке должно быть минимум 3 чата!")
        return

    selected_chats = random.sample(chat_ids, 3)  # Выбираем 3 случайных чата

    if not os.path.exists(GIF_PATH):
        print(f"Ошибка: Файл гифки '{GIF_PATH}' не найден!")
        return

    for chat_id in selected_chats:
        random_text = random.choice(WIN_MESSAGES)  # Выбираем случайное поздравление
        await client.send_file(chat_id, GIF_PATH, caption=random_text)
        print(f"Sent to chat {chat_id} with a hyphy")

def register_auto_reply(client):
    """Регистрирует триггер на слово 'тираж'."""
    
    @client.on(events.NewMessage(outgoing=True))
    async def check_raffle_trigger(event):
        """Запускает розыгрыш, если бот отправляет слово 'тираж'."""
        if "тираж" in event.message.text.lower():
            print("Launch the raffle!")
            await send_winner_messages(client)
