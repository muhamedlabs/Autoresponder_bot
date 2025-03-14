import os
import random
from telethon import events
from BANNED_FILES.config import IMAGE_applicationRU, IMAGE_applicationUK, IMAGE_applicationEN
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.application import get_translation


def register_proces(client):
    """Регистрирует команду 'БиоPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^БиоPro$"))
    async def send_bio(event):
        """Отправляет случайную фотографию Андрея Мухамеда как спойлер + биографию."""

        try:
            # Определяем язык пользователя, которому бот пишет
            user_id = event.chat_id
            lang = get_user_language(user_id) or "ru"

            # Получаем биографию на нужном языке
            bio_text = get_translation("biography_text", lang)

            # Если bio_text — список, превращаем его в строку
            if isinstance(bio_text, list):
                bio_text = "".join(bio_text)  # Объединяем список в строку

            # Проверяем, что bio_text - это строка
            if not isinstance(bio_text, str):
                print(f"Ошибка: get_translation('biography_text', {lang}) вернул {type(bio_text)}: {bio_text}")
                bio_text = "Информация временно недоступна."

            # Выбираем нужную папку по языку
            photo_mapping = {
                "ru": IMAGE_applicationRU,
                "uk": IMAGE_applicationUK,
                "en": IMAGE_applicationEN
            }
            photo_folder = photo_mapping.get(lang, IMAGE_applicationRU)  # Если нет языка, берём RU

            # Проверяем, существует ли папка
            if not os.path.exists(photo_folder):
                await event.respond(bio_text)  # Если папки нет, отправляем только текст
                return

            # Получаем список фото из папки
            photos = [
                f for f in os.listdir(photo_folder)
                if f.lower().endswith((".png", ".jpg", ".jpeg"))
            ]

            if photos:
                # Выбираем случайное фото
                random_photo = os.path.join(photo_folder, random.choice(photos))
                await event.client.send_file(
                    event.chat_id,
                    random_photo,
                    caption=bio_text,
                    spoiler=True
                )
            else:
                await event.respond(bio_text)  # Если фото нет, отправляем только текст

        except Exception as e:
            print(f"Ошибка при отправке биографии: {e}")