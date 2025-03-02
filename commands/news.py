from BANNED_FILES.config import VIDEO_newsRU, VIDEO_newsUK, VIDEO_newsEN
from language_file.UserLanguage import get_user_language
from language_file.news import get_translation



async def handle_news(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и видео
    video_dict = {
        "ru": VIDEO_newsRU,
        "uk": VIDEO_newsUK,
        "en": VIDEO_newsEN
    }

    # Выбираем нужное видео, если язык неизвестен — используем дефолтное
    VIDEO_news = video_dict.get(lang, VIDEO_newsRU)

    await client.send_message(
        chat_id,
        get_translation("television", lang),
        file=VIDEO_news  # Файл вашей видео
    )
