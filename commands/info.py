from BANNED_FILES.config import PHOTO_infoRU, PHOTO_infoUK, PHOTO_infoEN
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.info import get_translation



async def handle_info(client, chat_id, user_id, message_text):


    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_infoRU,
        "uk": PHOTO_infoUK,
        "en": PHOTO_infoEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_info = photo_dict.get(lang, PHOTO_infoRU)

    await client.send_message(
        chat_id,
        get_translation("information", lang),
        file=PHOTO_info  # Файл вашей картинки
    )