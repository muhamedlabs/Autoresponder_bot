import os
import random
from telethon import events
from BANNED_FILES.config import MEMES_FOLDER

def register_proces(client):
    """Регистрирует команду 'МемPro'."""

    @client.on(events.NewMessage(pattern=r"^МемPro$"))
    async def send_meme_voice(event):
        """Отправляет случайное голосовое сообщение в ответ на команду."""
        try:
            # Проверяем наличие папки с мемами
            if not os.path.exists(MEMES_FOLDER):
                print(f"Ошибка: Папка '{MEMES_FOLDER}' не найдена!")
                return
            
            # Собираем список файлов .ogg
            meme_files = [f for f in os.listdir(MEMES_FOLDER) if f.lower().endswith(".ogg")]
            
            if not meme_files:
                print("Ошибка: В папке нет файлов .ogg!")
                return

            # Выбираем случайное голосовое
            random_meme = random.choice(meme_files)
            meme_path = os.path.join(MEMES_FOLDER, random_meme)

            # Если команда отправлена в ответ на сообщение — отвечаем на него
            reply_to = event.reply_to_msg_id if event.reply_to_msg_id else None

            # Отправляем голосовое сообщение
            await event.client.send_file(event.chat_id, meme_path, voice_note=True, reply_to=reply_to)

        except Exception as e:
            print(f"Ошибка при отправке голосового мема: {e}")