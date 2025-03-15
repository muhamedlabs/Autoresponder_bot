import os 
import random
import os
from telethon import events
from BANNED_FILES.config import COTTAGE_IMAGE  # ОДИН конкретный файл
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.cottage import get_translation

def register_proces(client):
    """Регистрирует команду 'ДамойPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^ДамойPro$"))
    async def send_home_message(event):
        """Отправляет картинку с рандомным текстом."""

        user_id = event.chat_id
        lang = get_user_language(user_id)  # Получаем язык пользователя

        # Получаем случайное сообщение
        cottage_messages = get_translation("cottage_messages", lang)
        random_text = random.choice(cottage_messages) if cottage_messages else "Домой, БРО! 🏡"

        # Проверяем, существует ли файл
        if os.path.exists(COTTAGE_IMAGE) and os.path.isfile(COTTAGE_IMAGE):
            await event.client.send_file(event.chat_id, COTTAGE_IMAGE, caption=random_text)
        else:
            print(f"Ошибка: Файл '{COTTAGE_IMAGE}' не найден!")
            await event.respond(random_text)
