from telethon import events
import asyncio
import os
import random
from BANNED_FILES.config import ROBOTA_IMAGE, ROBOTA_MUSIC  # Импортируем пути к папкам
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.robota import get_translation

def register_proces(client):
    """Регистрирует авто-ответ на 'РоботаPro' с учётом регистра."""

    @client.on(events.NewMessage(outgoing=True))  # Бот реагирует на свои сообщения
    async def auto_reply(event):
        if "РоботаPro" in event.message.text:  # Убираем .lower(), теперь учитывается регистр
            await asyncio.sleep(1)

            # Берём ID получателя, а не отправителя
            user_id = event.chat_id
            lang = get_user_language(user_id)  # Используем функцию из отдельного файла

            # Случайное сообщение "Роботяги" на языке пользователя
            morning_message = random.choice(get_translation("robota_messages", lang))

            # Проверяем существование папки с картинками
            if not os.path.exists(ROBOTA_IMAGE):  # Используем ROBOTA_IMAGE
                print(f"Ошибка: Папка '{ROBOTA_IMAGE}' не найдена!")
                await event.respond(morning_message)
                return

            # Выбираем случайное фото
            images = [f for f in os.listdir(ROBOTA_IMAGE) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            if images:
                random_image = os.path.join(ROBOTA_IMAGE, random.choice(images))
                await event.client.send_file(event.chat_id, random_image, caption=morning_message)
            else:
                await event.respond(morning_message)
                print(f"Ответ на 'РоботаPro' без картинки (нет файлов в папке)")

            # Задержка 4 минуты 30 секунд перед отправкой песни
            await asyncio.sleep(270)

            # Проверяем существование папки с музыкой
            if not os.path.exists(ROBOTA_MUSIC):  # Используем ROBOTA_MUSIC
                print(f"Ошибка: Папка '{ROBOTA_MUSIC}' не найдена!")
                return

            # Выбираем случайную песню и комментарий
            songs = [f for f in os.listdir(ROBOTA_MUSIC) if f.lower().endswith((".mp3", ".wav", ".ogg"))]
            if songs:
                random_song = os.path.join(ROBOTA_MUSIC, random.choice(songs))
                song_comment = random.choice(get_translation("song_comments", lang))  # Случайный комментарий на языке пользователя
                await event.client.send_file(event.chat_id, random_song, caption=song_comment)
            else:
                print("Ошибка: В папке с музыкой нет файлов!")