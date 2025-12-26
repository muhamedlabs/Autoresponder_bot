import json
import os
from langdetect import detect, DetectorFactory
from langid.langid import LanguageIdentifier, model
from BANNED_FILES.config import DATA_FILE

DetectorFactory.seed = 0  # Фиксируем seed для langdetect
langid_identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)  # Инициализация langid


# Загружаем сохранённые данные
def load_user_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                data = file.read().strip()
                return json.loads(data) if data else {}
        except json.JSONDecodeError:
            print("Ошибка: повреждён файл user_languages.json. Пересоздаю.")
            return {}
    return {}


# Сохраняем данные
def save_user_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


async def get_user_language(client, user_id, message_text):
    """Определяет язык пользователя только по тексту."""

    user_data = load_user_data()

    # Если язык уже определён — используем его
    if str(user_id) in user_data:
        return user_data[str(user_id)]["language"]

    # Проверка длины сообщения
    if not message_text or len(message_text) < 3:
        return "ru"  # Если текст слишком короткий, ставим русский

    # Определение языка с langdetect
    try:
        detected_lang = detect(message_text)
    except:
        detected_lang = "unknown"

    # Определение языка с langid, если первый метод дал "unknown"
    if detected_lang not in ["ru", "en", "uk"]:
        detected_lang, _ = langid_identifier.classify(message_text)

    # Если язык неизвестен — ставим русский
    lang_code = detected_lang if detected_lang in ["ru", "en", "uk"] else "ru"

    # Сохраняем язык и первое сообщение
    user_data[str(user_id)] = {"language": lang_code, "first_message": message_text}
    save_user_data(user_data)

    return lang_code
