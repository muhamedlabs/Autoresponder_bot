from BANNED_FILES.config import PHOTO_faqRU, PHOTO_faqUK, PHOTO_faqEN
from language_file.transcribation.UserLanguage import get_user_language
from language_file.commands.faq import get_translation



async def handle_faq(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_faqRU,
        "uk": PHOTO_faqUK,
        "en": PHOTO_faqEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_faq = photo_dict.get(lang, PHOTO_faqRU)

    await client.send_message(
        chat_id,
        get_translation("queries", lang),
        file=PHOTO_faq  # Файл вашей картинки
    )