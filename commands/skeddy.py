import random
import os
from BANNED_FILES.config import VIDEO_skeddyRU, VIDEO_skeddyUK, VIDEO_skeddyEN
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.skeddy import get_translation

async def handle_skeddy(client, chat_id, user_id, message_text):
    # Определяем язык пользователя
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и папок с видео
    video_dict = {
        "ru": VIDEO_skeddyRU,  # Путь к папке с видео на русском
        "uk": VIDEO_skeddyUK,  # Путь к папке с видео на украинском
        "en": VIDEO_skeddyEN   # Путь к папке с видео на английском
    }

    # Выбираем папку с видео в зависимости от языка
    video_folder = video_dict.get(lang, VIDEO_skeddyRU)  # Если язык неизвестен, используем русский

    # Получаем список всех видеофайлов в папке
    if os.path.exists(video_folder):  # Проверяем, существует ли папка
        video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]  # Фильтруем по расширениям
    else:
        video_files = []  # Если папка не существует, список пуст

    # Если видео найдены, выбираем случайное
    if video_files:
        random_video = os.path.join(video_folder, random.choice(video_files))  # Полный путь к случайному видео
    else:
        random_video = None  # Если видео нет, используем None

    # Случайный выбор текста (цитаты)
    random_skeddy = random.choice(get_translation("skeddy", lang))

    # Отправка сообщения и видео
    if random_video:
        await client.send_file(chat_id, random_video, caption=random_skeddy)  # Отправляем видео с текстом
    else:
        await client.send_message(chat_id, random_skeddy)  # Если видео нет, отправляем только текст