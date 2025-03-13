import json
import os
from BANNED_FILES.config import DATA_FILE

def get_user_language(user_id):
    """
    Возвращает язык пользователя по его ID из файла user_languages.json.
    
    :param user_id: ID пользователя (должен быть строкой).
    :return: Язык пользователя (по умолчанию "ru").
    """
    try:
        if not os.path.exists(DATA_FILE):
            print(f"Файл {DATA_FILE} не найден!")
            return "ru"

        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                user_data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Ошибка JSON: {e}")
                return "ru"

        # **Добавляем защиту**
        if str(user_id) not in user_data:
            print(f"[DEBUG] Пользователь {user_id} не найден в базе. Используем 'ru'.")
            return "ru"

        return user_data[str(user_id)].get("language", "ru")

    except UnicodeEncodeError as e:
        print(f"Ошибка кодировки файла {DATA_FILE}: {e}")
        return "ru"
    except Exception as e:
        print(f"Ошибка при чтении файла {DATA_FILE}: {e}")
        return "ru"


