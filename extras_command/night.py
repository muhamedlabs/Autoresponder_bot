from telethon import events
import asyncio
import os
import random
from BANNED_FILES.config import NIGHT_IMAGE, NIGHT_MUSIC  # Импортируем пути к папкам
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.night import get_translation

def register_proces(client):
    """Регистрирует авто-ответ на 'НочьоPro' с учётом регистра."""

    @client.on(events.NewMessage(outgoing=True))  # Бот реагирует на свои сообщения
    async def auto_reply(event):
        if "НочьPro" in event.message.text:  # Убираем .lower(), теперь учитывается регистр
            await asyncio.sleep(1)

            # Берём ID получателя, а не отправителя
            user_id = event.chat_id 
            lang = get_user_language(user_id)  # Используем функцию из отдельного файла

            # Случайное сообщение "Сладких снов" на языке пользователя
            night_message = random.choice(get_translation("night_messages", lang))

            # Проверяем существование папки с картинками
            if not os.path.exists(NIGHT_IMAGE): 
                print(f"Ошибка: Папка '{NIGHT_IMAGE}' не найдена!")
                await event.respond(night_message)
                return

            # Выбираем случайное фото
            images = [f for f in os.listdir(NIGHT_IMAGE) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
            if images:
                random_image = os.path.join(NIGHT_IMAGE, random.choice(images))
                await event.client.send_file(event.chat_id, random_image, caption=night_message)
            else:
                await event.respond(night_message)
                print(f"Ответ на 'НочьPro' без картинки (нет файлов в папке)")

            # Задержка 2 минуты 30 секунд перед отправкой песни
            await asyncio.sleep(150)

            # Проверяем существование папки с музыкой
            if not os.path.exists(NIGHT_MUSIC):  # Используем MORNING_MUSIC
                print(f"Ошибка: Папка '{NIGHT_MUSIC}' не найдена!")
                return

            # Выбираем случайную песню и комментарий
            songs = [f for f in os.listdir(NIGHT_MUSIC) if f.lower().endswith((".mp3", ".wav", ".ogg"))]
            if songs:
                random_song = os.path.join(NIGHT_MUSIC, random.choice(songs))
                song_comment = random.choice(get_translation("song_comments", lang))  # Случайный комментарий на языке пользователя
                await event.client.send_file(event.chat_id, random_song, caption=song_comment)
            else:
                print("Ошибка: В папке с музыкой нет файлов!")