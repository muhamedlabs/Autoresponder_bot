from BANNED_FILES.config import PHOTO_chattingRU, PHOTO_chattingUK, PHOTO_chattingEN
from language_file.UserLanguage import get_user_language
from language_file.chatting import get_translation



async def handle_chatting(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_chattingRU,
        "uk": PHOTO_chattingUK,
        "en": PHOTO_chattingEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_chatting = photo_dict.get(lang, PHOTO_chattingRU)

    await client.send_message(
        chat_id,
        get_translation("correspondence", lang),
        file=PHOTO_chatting  # Файл вашей картинки
    )

