import os
from telethon import TelegramClient, events
from commands.handler import handle_command  # Command handler
from commands.pro_command.delete import register_auto_delete
from Ignore.config import phone_number, api_hash, api_id  # Config

# File for storing user data
FILE_NAME = "Ignore/Auto_users.txt"

# Path to the video file
VIDEO_FILE = "Видео_материал/MAIN.mp4"  # Set the correct path

# Creating the client only once
client = TelegramClient('session_name', api_id, api_hash)

async def get_user_id():
    me = await client.get_me()
    return me.id

async def main():
    # Connecting to Telegram
    try:
        await client.start(phone=lambda: phone_number)

        # Check for two-factor authentication
        if not await client.is_user_authorized():
            password = input("Enter your two-step verification password: ")
            await client.start(password=password)

        # Get the user ID and register auto-delete feature
        user_id = await get_user_id()
        register_auto_delete(client, user_id)

        print("Bot successfully launched!")
    except Exception as e:
        print(f"Authorization error: {e}")
        return

    print("Script is running. Waiting for new messages...")
    await client.run_until_disconnected()

# Registering auto-delete feature
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return  # Ignore messages from groups and channels

    sender = await event.get_sender()
    user_id = str(sender.id)  # User ID
    chat_id = event.chat_id   # Chat ID
    phone = sender.phone if sender.phone else "No phone number"
    username = sender.username if sender.username else "None"
    first_name = sender.first_name if sender.first_name else "None"
    last_name = sender.last_name if sender.last_name else "None"
    link = f"https://t.me/{username}" if username != "None" else "No link"

    # Load processed users
    def load_replied_users():
        if not os.path.exists(FILE_NAME):
            return {}
        users = {}
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split(",")
                user_id = parts[0].split(":")[1].strip()
                users[user_id] = line.strip()
        return users
    
    replied_users = load_replied_users()
    message_text = event.message.text.strip().lower()

    if message_text == "!старт":
        # Remove user from the list if they exist
        def remove_user_from_file(user_id):
            if not os.path.exists(FILE_NAME):
                return
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(FILE_NAME, "w", encoding="utf-8") as file:
                for line in lines:
                    if f"User ID: {user_id}" not in line:
                        file.write(line)
        remove_user_from_file(user_id)

        # Send video or text
        if os.path.exists(VIDEO_FILE):
            await client.send_file(
                chat_id,
                VIDEO_FILE,
                caption=(
                    "👹 **Путь начинается, воин!** Это автоматическое сообщение, которое отправляется без покупки **Telegram Premium**. "
                    "Мы больше не будем беспокоить вас, так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!инфо`, `!донат`, `!подарок`, `!боты` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://muhamedlabs.pro"
                ),
            )
        else:
            await event.reply("Файл видео отсутствует, но мы готовы вам помочь!")

        # Save user data
        def save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link):
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
        save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
        print(f"Данные пользователя сброшены: ID {user_id}, Телефон: {phone}, Имя: {first_name} {last_name}, Username: {username}")
    elif user_id not in replied_users:
        if os.path.exists(VIDEO_FILE):
            await client.send_file(
                chat_id,
                VIDEO_FILE,
                caption=(
                    "👹 **Путь начинается, воин!** Это автоматическое сообщение, которое отправляется без покупки **Telegram Premium**. "
                    "Мы больше не будем беспокоить вас, так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!инфо`, `!донат`, `!подарок`, `!боты` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://muhamedlabs.pro"
                ),
            )
        else:
            await event.reply("Файл видео отсутствует, но мы готовы вам помочь!")
        save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
        print(f"Сохранены данные пользователя: ID {user_id}, Телефон: {phone}, Имя: {first_name} {last_name}, Username: {username}")
    else:
        print(f"Сообщение от пользователя ID {user_id} пропущено: уже обработан.")
    if message_text.startswith("!"):
        await handle_command(client, chat_id, message_text)

if __name__ == "__main__":
    client.loop.run_until_complete(main())