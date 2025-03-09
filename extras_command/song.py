import os 
import random
from telethon import events

# Пути к файлам
IMAGE_PATH = os.path.abspath("Фото_материал/Photo_design/Цар.jpg")  # Определённая картинка
MUSIC_FOLDER = os.path.abspath("Подкаст_музика/Music_designer")  # Папка с музыкой

# Комментарии к песням
SONG_COMMENTS = [   
    "🎶🔥 Этот трек просто взрывает мозг! Каждая нота — это отдельная эмоция, которая пробирает до мурашек!",  
    "💖🎵 Музыка, которая не просто играет в наушниках, а остаётся в сердце! Такой вайб невозможно забыть!",  
    "😎🎧 Вот это настоящий хит! Включаешь и сразу погружаешься в другой мир, полный ритма и эмоций!",  
    "🚀 Бит этой песни будто отправляет в космос! Вибрации такие мощные, что хочется слушать на репите!",  
    "🔊 Ощущение, что музыка создана специально для тебя! Максимальный звук, полное погружение!",  
    "🎶💃 Этот ритм просто невозможно игнорировать! Хочется двигаться, подпевать, ощущать каждую ноту!",  
    "🌙🎵 Идеальный трек для уюта и расслабления. Закрываешь глаза и просто растворяешься в мелодии!",  
    "🎼✨ Гармония, которая вдохновляет! Это больше, чем музыка — это волшебство, которое оживает в каждой секунде!",  
    "🎧🔥 Только включил, а уже чувствую, как этот трек становится моим любимым! Гениально, стильно, мощно!",  
    "🎵🔮 Музыкальная магия в чистом виде! Слушаешь и понимаешь, что настоящая музыка способна творить чудеса!"  
]   

def register_auto_reply(client):
    """Регистрирует команду 'ПесняPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^ПесняPro$"))
    async def send_songs(event):
        """Отправляет определённую картинку и 3 случайные песни с подписями."""
        
        # Отправляем картинку без подписи
        if os.path.exists(IMAGE_PATH):
            await event.client.send_file(event.chat_id, IMAGE_PATH)
            print(f"A picture has been sent: {IMAGE_PATH}")
        else:
            print(f"Ошибка: Файл '{IMAGE_PATH}' не найден!")

        # Проверяем наличие папки с музыкой
        if not os.path.exists(MUSIC_FOLDER):
            print(f"Ошибка: Папка '{MUSIC_FOLDER}' не найдена!")
            return

        songs = [f for f in os.listdir(MUSIC_FOLDER) if f.lower().endswith((".mp3", ".wav", ".ogg"))]

        # Проверяем наличие музыки
        if len(songs) < 3:
            print("Ошибка: В папке с музыкой меньше 3 файлов!")
            return

        # Выбираем 3 случайных песни
        random_songs = random.sample(songs, 3)

        # Отправляем каждую песню с подписью
        for song in random_songs:
            random_comment = random.choice(SONG_COMMENTS)
            song_path = os.path.join(MUSIC_FOLDER, song)
            await event.client.send_file(event.chat_id, song_path, caption=random_comment)
            print(f"Song Sent: {song_path}")