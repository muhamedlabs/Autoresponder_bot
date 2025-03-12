import os
import random
from BANNED_FILES.config import AUDIO_FILE, PODCAST_FILE
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.podcast import get_translation



async def handle_podcast(client, chat_id, user_id, message_text):
    """Обработчик команды подкаста с отправкой случайного аудиофайла."""

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)
    
    # Получаем список файлов с расширением .ogg
    audio_files = [f for f in os.listdir(AUDIO_FILE) if f.endswith(".ogg")]
    
    # Если нет доступных подкастов
    if not audio_files:
        await client.send_message(
            chat_id,
            get_translation("no_podcast", lang),
            file=PODCAST_FILE
        )
        return
    
    # Выбираем случайный файл, гарантируя, что это будет новый случайный файл каждый раз
    random_audio = random.choice(audio_files)
    audio_path = os.path.join(AUDIO_FILE, random_audio)
    
    # Отправляем сообщение с текстом и видео когда есть подкаст
    await client.send_message(
        chat_id,
        get_translation("is_podcast", lang),
        file=PODCAST_FILE
    )
    
    # Отправляем голосовое сообщение
    await client.send_file(
        chat_id,
        file=audio_path,
        voice_note=True  # Отправляем файл как голосовое сообщение
    )
