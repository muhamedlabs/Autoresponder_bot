from langdetect import detect, DetectorFactory
from langid.langid import LanguageIdentifier, model
from ashredis import MISSING
from BANNED_FILES.config import RedisManager
from redis_storage.users_contest import UsersContest

DetectorFactory.seed = 0
langid_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

redis = RedisManager()

async def get_user_language(client, user_id: str, message_text: str):
    """
    Визначає мову користувача, зберігає її в Redis
    та записує перші 5 повідомлень.
    """

    # Якщо текст порожній або короткий — вважаємо, що це "ru"
    if not message_text or len(message_text.strip()) < 3:
        message_text = ""
        lang_code = "ru"
    else:
        # Пробуємо визначити мову через langdetect
        try:
            detected_lang = detect(message_text)
        except Exception:
            detected_lang = "unknown"

        # Якщо результат неочевидний — дублюємо через langid
        if detected_lang not in ["ru", "en", "uk"]:
            detected_lang, _ = langid_identifier.classify(message_text)

        lang_code = detected_lang if detected_lang in ["ru", "en", "uk"] else "ru"

    # Завантажуємо запис користувача з Redis
    async with redis:
        record = await redis.load(UsersContest, key=str(user_id))

        if record is None:
            # Новий користувач → створюємо новий запис
            record = UsersContest(
                user_id=str(user_id),
                language=lang_code,
                first_name=None
            )
        else:
            # Якщо мова вже є — не оновлюємо її
            if not record.language:
                record.language = lang_code

        # Зберігаємо перші 5 повідомлень
        for i in range(1, 6):
            field_name = f"first_message_{i}"
            current_value = getattr(record, field_name, MISSING)
            if current_value in [None, "", MISSING]:
                setattr(record, field_name, message_text)
                break

        # Зберігаємо назад у Redis
        await redis.save(record, key=str(user_id))

    return record.language
