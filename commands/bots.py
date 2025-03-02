from BANNED_FILES.config import PHOTO_botsRU, PHOTO_botsUK, PHOTO_botsEN
from language_file.UserLanguage import get_user_language
from language_file.bots import get_translation



async def handle_bots(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_botsRU,
        "uk": PHOTO_botsUK,
        "en": PHOTO_botsEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_bots = photo_dict.get(lang, PHOTO_botsRU)

    await client.send_message(
        chat_id,
        get_translation("programs", lang),
        file=PHOTO_bots  # Файл вашей картинки
    )
