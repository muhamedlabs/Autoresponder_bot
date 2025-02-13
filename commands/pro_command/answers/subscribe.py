import asyncio
import os
import random
import re
from telethon import events

# Файл со списком пользователей
CHAT_FILE = "Ignore/Auto_users.txt"  # Файл с ID чатов
GIF_PATH = os.path.abspath("Видео_материал/Gif/Virus.gif")  # Путь к гифке

WELCOME_MESSAGES = [  
    "**Ну всё, ты попался! 😈**\n\nТы так долго игнорил нас, что теперь подхватил ВИРУС! 🦠 Но не переживай, есть способ его удалить... 😏\n\n✅ Просто подпишись на наши проекты и заходи на сайт: https://muhamedlabs.pro",  

    "**О нет, вирус атаковал! 💀**\n\nТы забыл про нас? Ну вот, теперь твоя система заражена! 😱 Единственный способ избавиться от вируса — подписаться на мои проекты! 🚀\n\n🎯 Спасайся тут: https://muhamedlabs.pro",  

    "**Ошибка 404? Нет, вирус 100%! 🔥**\n\nТы нас так долго игнорил, что система решила отомстить! 😈 Теперь у тебя вирус, и удалить его можно только одним способом... ПОДПИСКОЙ! 😏\n\n✅ Спасайся тут: https://muhamedlabs.pro",  

    "**Тревога! 🚨 Ты заражён!**\n\nМы предупреждали… но ты не слушал! Теперь у тебя вирус! 🦠 Чтобы его удалить, срочно подписывайся на наши проекты и заходи на сайт! 🔥\n\n🌍 Вот спасение: https://muhamedlabs.pro",  

    "**Вирус активирован! 💀**\n\nТвоя система в опасности! 🦠 Единственный антивирус — подписка на мои проекты! Подписывайся скорее, пока не стало хуже! 😏\n\n⚡ Жми сюда: https://muhamedlabs.pro",  
]  

# Функция загрузки списка чатов из файла
def load_chat_ids():
    if not os.path.exists(CHAT_FILE):
        print(f"Ошибка: Файл '{CHAT_FILE}' не найден!")
        return []
    
    with open(CHAT_FILE, "r", encoding="utf-8") as file:
        content = file.read()

    chat_ids = re.findall(r"ID чата: (\d+)", content)  # Регулярка для поиска ID
    return list(map(int, chat_ids))  # Преобразуем в список чисел

async def send_welcome_message(client):
    """Отправляет сообщение только 1 случайному участнику."""
    chat_ids = load_chat_ids()
    
    if not chat_ids:
        print("Ошибка: Список пользователей пуст!")
        return

    selected_chat = random.choice(chat_ids)  # Выбираем ОДИН случайный чат

    if not os.path.exists(GIF_PATH):
        print(f"Ошибка: Файл гифки '{GIF_PATH}' не найден!")
        return

    welcome_text = random.choice(WELCOME_MESSAGES)  # Выбираем случайное приветствие
    await client.send_file(selected_chat, GIF_PATH, caption=welcome_text)
    print(f"Sent to {selected_chat} chat with a hyphy")

def register_auto_reply(client):
    """Регистрирует триггер на слово 'ронин'."""
    
    @client.on(events.NewMessage(outgoing=True))
    async def check_raffle_trigger(event):
        """Запускает процесс выбора нового подписчика при слове 'ронин'."""
        if "ронин" in event.message.text.lower():
            print("New-to-old subscriber's choice!")
            await send_welcome_message(client)
