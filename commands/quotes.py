import random
import os
from BANNED_FILES.config import QUOTES_FILE
from language_file.UserLanguage import get_user_language
from language_file.quotes import get_translation

async def handle_quotes(client, chat_id, user_id, message_text):
    # Определяем язык пользователя
    lang = await get_user_language(client, user_id, message_text)

    # Получаем список всех видеофайлов в папке
    if os.path.exists(QUOTES_FILE):  # Проверяем, существует ли папка
        video_files = [f for f in os.listdir(QUOTES_FILE) if f.endswith(('.mp4', '.avi', '.mkv'))]  # Фильтруем по расширениям
    else:
        video_files = []  # Если папка не существует, список пуст

    # Если видео найдены, выбираем случайное
    if video_files:
        random_video = os.path.join(QUOTES_FILE, random.choice(video_files))  # Полный путь к случайному видео
    else:
        random_video = None  # Если видео нет, используем None

    # Случайный выбор цитаты
    random_quote = random.choice(get_translation("quotes", lang))

    # Отправка цитаты и видео
    if random_video:
        await client.send_file(chat_id, random_video, caption=random_quote)  # Отправляем видео с цитатой
    else:
        await client.send_message(chat_id, random_quote)  # Если видео нет, отправляем только цитату