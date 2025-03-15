import os
import random
from telethon import events
from BANNED_FILES.config import INTERMISSION_IMAGE, INTERMISSION_MUSIC
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.intermission import get_translation

def register_proces(client):
    """Регистрирует команду 'АнтрактPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^АнтрактPro$"))
    async def send_songs(event):
        """Отправляет картинку и 3 случайные песни с подписями на языке пользователя."""

        user_id = event.chat_id
        lang = get_user_language(user_id)  # Определяем язык пользователя

        # Текст-подпись к картинке
        image_caption = get_translation("image_caption", lang)

        # **Отправка картинки**
        if os.path.exists(INTERMISSION_IMAGE) and os.path.isfile(INTERMISSION_IMAGE):
            await event.client.send_file(event.chat_id, INTERMISSION_IMAGE, caption=image_caption)
        else:
            print(f"Ошибка: Файл '{INTERMISSION_IMAGE}' не найден!")

        # **Проверка папки с музыкой**
        if not os.path.exists(INTERMISSION_MUSIC):
            print(f"Ошибка: Папка '{INTERMISSION_MUSIC}' не найдена!")
            return

        songs = [f for f in os.listdir(INTERMISSION_MUSIC) if f.lower().endswith((".mp3", ".wav", ".ogg"))]

        # **Проверка наличия хотя бы 3 песен**
        if len(songs) < 3:
            print("Ошибка: В папке с музыкой меньше 3 файлов!")
            return

        # **Выбираем 3 случайные песни**
        random_songs = random.sample(songs, 3)

        # **Отправляем каждую песню с подписью**
        for song in random_songs:
            song_comment = random.choice(get_translation("song_comments", lang))
            song_path = os.path.join(INTERMISSION_MUSIC, song)
            await event.client.send_file(event.chat_id, song_path, caption=song_comment, parse_mode=None)
