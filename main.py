import os
from telethon import TelegramClient, events
from commands.handler import handle_command  # Import command handler
from Ignore.config import phone_number, api_hash, api_id # Import config

# File for storing user data
FILE_NAME = "Ignore/Auto_users.txt"

# Path to the video file
VIDEO_FILE = "Видео_материал/MAIN.mp4"  # Replace with your path

# Function to load already processed users
def load_replied_users():
    if not os.path.exists(FILE_NAME):
        return set()
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        users = set(line.split(",")[0].split(":")[1].strip() for line in file if line.strip())
    return users

# Function to save user data
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

# Create the client
client = TelegramClient('session_name', api_id, api_hash)

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

    replied_users = load_replied_users()

    if user_id not in replied_users:  # If the user is new
        # Send video or text
        if os.path.exists(VIDEO_FILE):  # Check if the video exists
            await client.send_file(
                chat_id,
                VIDEO_FILE,
                caption=(
                    "👹 **Путь начинается, воин!** Это автоматическое сообщение, которое отправляется без покупки **Telegram Premium**. "
                    "Мы больше не будем беспокоить вас, так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!инфо`, `!донат`, `!подарок`, `!боты` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://andremuhamed.pro"
                ),
            )
        else:
            await event.reply("The video file is missing, but we're here to assist you!")

        # Save user data
        save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
        print(f"Saved user data: ID {user_id}, Phone: {phone}, Name: {first_name} {last_name}, Username: {username}")
    else:
        print(f"Message from user ID {user_id} skipped: already processed.")

    # Process commands
    message_text = event.message.text.strip()
    if message_text.startswith("!"):
        await handle_command(client, chat_id, message_text.lower())

async def main():
    # Attempt to connect to Telegram
    try:
        await client.start(phone=lambda: phone_number)

        # Check for two-factor authentication
        if not await client.is_user_authorized():
            password = input("Enter your two-step verification password: ")
            await client.start(password=password)

        print("Authorization successful!")
    except Exception as e:
        print(f"Authorization error: {e}")
        return

    print("Script is running. Waiting for new messages...")
    await client.run_until_disconnected()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
