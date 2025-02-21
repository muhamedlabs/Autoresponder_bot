import os 
import random
from telethon import events

# Пути к папке с видео и файлу с текстами
VIDEO_FOLDER = os.path.abspath("Видео_материал/Skeddy")  # Укажи правильный путь к видео
TEXT_FILE = os.path.abspath("Ignore/Skeddy_texts.txt")  # Файл с текстами

def register_ideas_plans(client):
    """Регистрирует команду '/skeddy'."""

    @client.on(events.NewMessage(pattern=r"^/skeddy$"))  # Работает для всех сообщений
    async def skeddy_command(event):
        """Отправляет случайное видео и текст из файла."""

        # Проверяем наличие папки с видео
        if not os.path.exists(VIDEO_FOLDER):
            print(f"Ошибка: Папка '{VIDEO_FOLDER}' не найдена!")
            return

        # Получаем список видеофайлов
        videos = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith((".mp4", ".mov", ".avi", ".mkv"))]

        if not videos:
            print("Ошибка: В папке нет видеофайлов!")
            return

        # Выбираем случайное видео
        random_video = os.path.join(VIDEO_FOLDER, random.choice(videos))

        # Читаем текст из файла
        if not os.path.exists(TEXT_FILE):
            print(f"Ошибка: Файл '{TEXT_FILE}' не найден!")
            return

        with open(TEXT_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            texts = [line.strip() for line in lines if line.strip()]

        if not texts:
            print("Ошибка: Файл с текстами пуст или содержит только пробелы!")
            return

        # Выбираем случайный текст
        random_text = random.choice(texts)

        # Отправляем видео с текстом
        await event.client.send_file(event.chat_id, random_video, caption=random_text)
        print(f"Отправлено видео с планами и идеями Мухамеда!")