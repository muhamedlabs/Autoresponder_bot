import requests 
from Ignore.config import UNSPLASH_ACCESS_KEY

async def handle_picture(client, chat_id):
    """Обработчик команды !картинка для отправки случайной картинки с Unsplash."""
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

        # Формируем сообщение с изображением
        await client.send_message(
            chat_id,
            (
                f"🌍 **Удивительные моменты от сервера Unsplash**\n\n"
                f"Смотреть изображение: [тут]({image_url})\n\n"
                f"Автор: [{author}]({author_url})\n\n"
                f"Описание: {description}\n\n"
            ),
            parse_mode="markdown"
        )

    except Exception as e:
        # Обработка ошибок
        await client.send_message(
            chat_id,
            (
                "❌ **Ошибка при загрузке изображения**\n\n"
                "К сожалению, сейчас мы не можем загрузить новое изображение. "
                "Попробуйте снова через некоторое время.\n\n"
                "Мы всегда стремимся радовать вас лучшими моментами!"
            )
        )
        print(f"Ошибка: {e}")


