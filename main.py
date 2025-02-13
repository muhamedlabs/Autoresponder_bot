import os
import asyncio
from telethon import TelegramClient, events
from commands.handler import handle_command
from Ignore.config import phone_number, api_hash, api_id
from commands.pro_command.delete import register_auto_delete  # Импорт авто-удаления
from commands.pro_command.comment import register_comment_handler # Импорт коментов
from commands.pro_command.answers.auto_loader import load_auto_responses # Импорт авто-ответ

# Файл для хранения данных пользователей
FILE_NAME = "Ignore/Auto_users.txt"

# Путь к видеофайлу
VIDEO_FILE = "Видео_материал/MAIN.mp4"

# Создание клиента
client = TelegramClient('session_name', api_id, api_hash)

# Подключаем авто-удаление
register_auto_delete(client)

# Подключение комментариев
register_comment_handler(client)

# Загружаем автоответы
load_auto_responses(client)

def load_replied_users():
    """Загружает список пользователей, которым уже отправлялось сообщение."""
    if not os.path.exists(FILE_NAME):
        return {}

    users = {}
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split(",")
            user_id = parts[0].split(":")[1].strip()
            users[user_id] = line.strip()

    return users


def save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link):
    """Сохраняет данные пользователя."""
    with open(FILE_NAME, "a", encoding="utf-8") as file:
        file.write(
            f"ID пользователя: {user_id}, "
            f"Имя пользователя: {username}, "
            f"Имя: {first_name}, "
            f"Фамилия: {last_name}, "
            f"Телефон: {phone}, "
            f"ID чата: {chat_id}, "
            f"Ссылка: {link}\n"
        )


def remove_user_from_file(user_id):
    """Удаляет пользователя из списка, если он вызывает !старт."""
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for line in lines:
            if f"ID пользователя: {user_id}" not in line:
                file.write(line)


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return  # Игнорируем сообщения из групп

    sender = await event.get_sender()
    if sender is None:
        print("Ошибка: Не удалось получить отправителя.")
        return

    user_id = str(sender.id)  # ID пользователя
    chat_id = event.chat_id  # ID чата
    phone = sender.phone if sender.phone else "No phone number"
    username = sender.username if sender.username else "None"
    first_name = sender.first_name if sender.first_name else "None"
    last_name = sender.last_name if sender.last_name else "None"
    link = f"https://t.me/{username}" if username != "None" else "No link"

    replied_users = load_replied_users()
    message_text = event.message.text.strip().lower() if event.message.text else ""

    if message_text == "!старт":
        remove_user_from_file(user_id)

        # Отправляем видео
        if os.path.exists(VIDEO_FILE):
            await client.send_file(
                chat_id,
                VIDEO_FILE,
                caption=(
                    "👹 **Путь начинается, воин!** Это автоматическое сообщение, "
                    "которое отправляется без покупки **Telegram Premium**. Мы больше не будем беспокоить вас, "
                    "так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!инфо, `!донат`, `!подарок`, `!боты` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://muhamedlabs.pro"
                ),
            )
        else:
            await event.reply("Файл видео отсутствует, но мы готовы вам помочь!")

        save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
        print(f"Данные пользователя сброшены: ID {user_id}, Телефон: {phone}, Имя: {first_name} {last_name}, Username: {username}")

    elif user_id not in replied_users:
        if os.path.exists(VIDEO_FILE):
            await client.send_file(
                chat_id,
                VIDEO_FILE,
                caption="👹 **Путь начинается, воин!** Это автоматическое сообщение, "
                    "которое отправляется без покупки **Telegram Premium**. Мы больше не будем беспокоить вас, "
                    "так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!инфо`, `!донат`, `!подарок`, `!боты` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://muhamedlabs.pro"
            )
        else:
            await event.reply("Файл видео отсутствует, но мы готовы вам помочь!")

        save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
        print(f"Сохранены данные пользователя: ID {user_id}, Телефон: {phone}, Имя: {first_name} {last_name}, Username: {username}")

    else:
        print(f"Сообщение от пользователя ID {user_id} пропущено: уже обработан.")

    # Проверяем команды
    if message_text.startswith("!"):
        await handle_command(client, chat_id, message_text)


async def main():
    try:
        await client.start(phone=lambda: phone_number)

        if not await client.is_user_authorized():
            password = input("Введите пароль двухфакторной аутентификации: ")
            await client.start(password=password)

        print("The bot has been successfully launched!")
    except Exception as e:
        print(f"Ошибка авторизации: {e}")
        return

    print("Script is running. Waiting for messages...")
    await client.run_until_disconnected()


if __name__ == "__main__":
    client.loop.run_until_complete(main())