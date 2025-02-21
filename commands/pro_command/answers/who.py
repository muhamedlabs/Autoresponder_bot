import os 
import random
from telethon import events

# Путь к папке с фотографиями
PHOTO_FOLDER = os.path.abspath("Фото_материал/Photo_design/Андрей Мухамед")

# Автобиография Андрея Мухамеда
BIOGRAPHY = (
    "**Андрей Мухамед — креативный предприниматель и вдохновитель инновационных проектов.**\n\n"
    "🌟 Его деятельность охватывает **рекламу, технологии и цифровой контент**, объединяя идеи и возможности, чтобы создавать нечто уникальное.\n\n"
    "**Владелец пяти динамично развивающихся каналов:**\n"
    "— 🎮 __Game Quest__ - всё о видеоиграх и их индустрии;\n"
    "— 🔥 __Nanson__ - актуальные песни без ап;\n"
    "— 🎌 __ANIME INDUSTRY__ - мир подборок новинок аниме;\n"
    "— 🎥 __KINO INDUSTRY__ - новинки кино, сериалов и мультфильмов;\n"
    "— 🎧 __Стримус__ - просто стримы от души.\n\n"
    "💻 Помимо этого, Андрей активно занимается **программированием, управлением соцсетями, рекламой, написанием сценариев, видеомонтажом и созданием контента**.\n\n"
    "**Его главная цель — вдохновлять и создавать что-то** [новое!](https://muhamedlabs.pro)"
)

def register_auto_reply(client):
    """Регистрирует команду 'КтоPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^КтоPro$"))
    async def send_bio(event):
        """Отправляет случайную фотографию Андрея Мухамеда как спойлер + биографию."""

        # Проверяем, существует ли папка с фото
        if not os.path.exists(PHOTO_FOLDER):
            print(f"Ошибка: Папка '{PHOTO_FOLDER}' не найдена!")
            await event.respond(BIOGRAPHY)  # Если папки нет, просто отправляем текст
            return

        # Получаем список фото из папки
        photos = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

        if photos:
            # Выбираем случайную фотографию
            random_photo = os.path.join(PHOTO_FOLDER, random.choice(photos))
            await event.client.send_file(
                event.chat_id, random_photo, caption=BIOGRAPHY, spoiler=True
            )
            print(f"Фото отправлено как спойлер: {random_photo}")
        else:
            await event.respond(BIOGRAPHY)  # Если фото нет, просто отправляем текст
            print("Ошибка: В папке нет фотографий!")