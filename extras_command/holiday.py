import os
import random
import re
from telethon import events
from BANNED_FILES.config import HOLIDAY_GIF  # Путь к гифке
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.holiday import get_translation

def register_proces(client):
    """Регистрирует автоответ на команду 'ВиходнойPro'."""

    @client.on(events.NewMessage(outgoing=True))
    async def weekend_reply(event):
        if event.message.text.strip() == "ВиходнойPro":
            # Игнорируем сообщения из групп и каналов
            if event.is_group or event.is_channel:
                print("Игнорируем сообщение в группе/канале")
                return  

            user_id = event.chat_id
            lang = get_user_language(user_id)  # Получаем язык пользователя
            weekend_messages = get_translation("holiday_messages", lang)  # Берём список фраз

            if not weekend_messages or not isinstance(weekend_messages, list):
                print("Ошибка: 'weekend_messages' не найден или имеет неверный формат!")
                return

            random_text = random.choice(weekend_messages)  # Берём случайное сообщение

            if not os.path.exists(HOLIDAY_GIF):  # Проверяем существование гифки
                print(f"Ошибка: Файл '{HOLIDAY_GIF}' не найден!")
                await event.respond(random_text)
                return

            await event.client.send_file(event.chat_id, HOLIDAY_GIF, caption=random_text)
