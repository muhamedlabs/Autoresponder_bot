import os
import random
import re
from telethon import events
from BANNED_FILES.config import GETAWAY_GIF  # Путь к гифке
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.getaway import get_translation

def register_proces(client):
    """Регистрирует автоответ на команду 'ОтпускPro'."""

    @client.on(events.NewMessage(outgoing=True))
    async def weekend_reply(event):
        if event.message.text.strip() == "ОтпускPro":
            # Игнорируем сообщения из групп и каналов
            if event.is_group or event.is_channel:
                print("Игнорируем сообщение в группе/канале")
                return  

            user_id = event.chat_id
            lang = get_user_language(user_id)  # Получаем язык пользователя
            vacation_messages = get_translation("getaway_messages", lang)  # Берём список фраз

            if not vacation_messages or not isinstance(vacation_messages, list):
                print("Ошибка: 'getaway_messages' не найден или имеет неверный формат!")
                return

            random_text = random.choice(vacation_messages)  # Берём случайное сообщение

            if not os.path.exists(GETAWAY_GIF):  # Проверяем существование гифки
                print(f"Ошибка: Файл '{GETAWAY_GIF}' не найден!")
                await event.respond(random_text)
                return

            await event.client.send_file(event.chat_id, GETAWAY_GIF, caption=random_text)