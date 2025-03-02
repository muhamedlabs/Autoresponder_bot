from BANNED_FILES.config import PHOTO_daisyRU, PHOTO_daisyUK, PHOTO_daisyEN
from language_file.UserLanguage import get_user_language
from language_file.donate import get_translation


async def handle_donate(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_daisyRU,
        "uk": PHOTO_daisyUK,
        "en": PHOTO_daisyEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_daisy = photo_dict.get(lang, PHOTO_daisyRU)

    await client.send_message(
        chat_id,
        get_translation("money", lang),
        file=PHOTO_daisy  # Файл вашей картинки
    )
