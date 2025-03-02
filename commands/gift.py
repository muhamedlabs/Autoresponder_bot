from BANNED_FILES.config import PHOTO_giftRU, PHOTO_giftUK, PHOTO_giftEN
from language_file.UserLanguage import get_user_language
from language_file.gift import get_translation



async def handle_gift(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_giftRU,
        "uk": PHOTO_giftUK,
        "en": PHOTO_giftEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_gift = photo_dict.get(lang, PHOTO_giftRU)

    await client.send_message(
        chat_id,
        get_translation("grant", lang),
        file=PHOTO_gift  # Файл вашей картинки
    )

