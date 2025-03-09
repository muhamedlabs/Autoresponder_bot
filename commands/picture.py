import requests
from BANNED_FILES.config import UNSPLASH_ACCESS_KEY
from language_file.UserLanguage import get_user_language
from language_file.picture import get_translation

async def handle_picture(client, chat_id, user_id, message_text):
    """Обработчик команды !picture для отправки случайной картинки с Unsplash."""
    
    # Определяем язык пользователя
    lang = await get_user_language(client, user_id, message_text)
    
    # Запрос к API Unsplash для случайного изображения по тематикам
    url = "https://api.unsplash.com/photos/random"
    query_params = {
        "query": "architecture,nature,trains",  # Темы: архитектура, природа, поезда
        "client_id": UNSPLASH_ACCESS_KEY,
        "orientation": "landscape",  # Горизонтальная ориентация
    }

    try:
        # Выполняем запрос
        response = requests.get(url, params=query_params)
        response.raise_for_status()  # Проверяем наличие ошибок HTTP
        data = response.json()

        # Извлекаем URL изображения
        image_url = data["urls"]["regular"]
        description = data.get("description", "Прекрасное изображение") or "Красота вокруг нас"
        author = data["user"]["name"]
        author_url = data["user"]["links"]["html"]

        # Получаем перевод сообщения
        message_text = get_translation("image_caption", lang).format(
            image_url=image_url, author=author, author_url=author_url, description=description
        )

        # Отправляем сообщение
        await client.send_message(chat_id, message_text, parse_mode="markdown")

    except Exception as e:
        # Обрабатываем ошибку с переводом
        error_message = get_translation("error_message", lang)
        await client.send_message(chat_id, error_message)
        print(f"Ошибка: {e}")