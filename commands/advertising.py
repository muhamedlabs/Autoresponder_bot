from BANNED_FILES.config import PHOTO_advertisingRU, PHOTO_advertisingUK, PHOTO_advertisingEN
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.advertising import get_translation



async def handle_advertising(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_advertisingRU,
        "uk": PHOTO_advertisingUK,
        "en": PHOTO_advertisingEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_advertising = photo_dict.get(lang, PHOTO_advertisingRU)

    await client.send_message(
        chat_id,
        get_translation("extension", lang),
        file=PHOTO_advertising  # Файл вашей картинки
    )