import random
import os
from BANNED_FILES.config import QUOTES_FILE
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.quotes import get_translation

async def handle_quotes(client, chat_id, user_id, message_text):
    # Определяем язык пользователя
    lang = await get_user_language(client, user_id, message_text)

    # Случайный выбор цитаты
    random_quote = random.choice(get_translation("quotes", lang))

    # Проверяем, существует ли видео
    if os.path.exists(QUOTES_FILE):  # Проверяем, существует ли файл
        await client.send_file(chat_id, QUOTES_FILE, caption=random_quote)  # Отправляем видео с цитатой
    else:
        await client.send_message(chat_id, random_quote)  # Если видео нет, отправляем только цитату