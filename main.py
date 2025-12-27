import os
import asyncio
import langdetect
import langid
import zipfile
import tempfile
from datetime import datetime

from telethon import TelegramClient, events, types
from telethon.errors import YouBlockedUserError, SessionPasswordNeededError

from BANNED_FILES.config import phone_number, api_hash, api_id, FILE_NAME, VIDEO_FILE
from commands.UserHandler import handle_command  # Загрузка основных команд
from language_file.transcribation.UserLanguage import get_user_language  # Загрузка определения языка
from extras_command.UserProces import load_proces  # Загрузка доп команд
from extras_command.UserRemover import load_remover  # Загрузка автоудаления команд
from extras_command.UserNotes import load_сomment  # Загрузка комментариев от пользователей
from language_file.main import get_translation  # Загрузка транскрипции
from extras_command.ads_command import load_ads_command  # Загрузка архиватора


# Инициализация клиента
client = TelegramClient("session_name", api_id, api_hash)


async def initialize_commands():
    """Инициализация всех команд бота"""

    # Подключение архиватора
    await load_ads_command(client)

    # Подключение автоудаления команд
    load_remover(client)

    # Подключение доп команд
    load_proces(client)

    # Подключение комментариев от пользователей
    load_сomment(client)


def load_replied_users():
    """Загрузка пользователей, которым уже отправлялось приветствие"""
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return {line.split(",")[0].split(":")[1].strip() for line in file}
    except Exception as e:
        print(f"Ошибка загрузки пользователей: {e}")
    return set()


def save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link):
    """Сохраняет данные нового пользователя"""
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(
                f"ID пользователя: {user_id}, "
                f"Username: {username}, "
                f"Имя: {first_name}, "
                f"Фамилия: {last_name}, "
                f"Телефон: {phone}, "
                f"ID чата: {chat_id}, "
                f"Ссылка: {link}\n"
            )
    except Exception as e:
        print(f"Ошибка сохранения пользователя: {e}")


def remove_user_from_file(user_id):
    """Удаляет пользователя из файла после команды !start"""
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                lines = file.readlines()

            with open(FILE_NAME, "w", encoding="utf-8") as file:
                for line in lines:
                    if f"ID пользователя: {user_id}" not in line:
                        file.write(line)
    except Exception as e:
        print(f"Ошибка удаления пользователя: {e}")


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    """Основной обработчик входящих сообщений"""
    if not event.is_private:
        return

    sender = await event.get_sender()
    if sender is None:
        print("Ошибка: Не удалось получить отправителя.")
        return

    user_id = str(sender.id)
    chat_id = event.chat_id
    phone = sender.phone if sender.phone else "No phone number"
    username = sender.username if sender.username else "None"
    first_name = sender.first_name if sender.first_name else "None"
    last_name = sender.last_name if sender.last_name else "None"
    link = f"https://t.me/{username}" if username != "None" else "No link"

    replied_users = load_replied_users()
    message_text = event.message.text.strip().lower() if event.message.text else ""

    # Определяем язык пользователя
    lang = await get_user_language(client, user_id, message_text)

    if message_text == "!start":
        remove_user_from_file(user_id)
        replied_users.discard(user_id)

    if user_id not in replied_users:
        try:
            if os.path.exists(VIDEO_FILE):
                await client.send_file(
                    chat_id,
                    VIDEO_FILE,
                    caption=get_translation("welcome", lang)
                )
            else:
                await event.reply(get_translation("welcome", lang))

            save_replied_user(user_id, username, first_name, last_name, phone, chat_id, link)
            print(f"Сохранены данные пользователя: {user_id}, Имя пользователя: {username}, Ссылка: {link}")

        except YouBlockedUserError:
            print(f"Пользователь {user_id} заблокировал бота или бот заблокировал пользователя.")
        except Exception as e:
            print(f"Не удалось отправить приветственное сообщение: {e}")

    if message_text.startswith("!"):
        command = message_text.split()[0]
        await handle_command(client, chat_id, user_id, command, message_text)


async def main():
    """Запуск бота"""
    try:
        await client.connect()

        print("Checking authorization...")
        # Авторизация
        while not await client.is_user_authorized():
            try:
                await client.send_code_request(phone_number)
                print("Code request sent. Waiting for code...")
                code_file = "code.txt"
                if os.path.exists(code_file):
                    with open(code_file, "r") as f:
                        code = f.read().strip()
                    os.remove(code_file)  # Удаляем файл после чтения
                    print(f"Code read from file: {code}")
                else:
                    code = await asyncio.to_thread(input, "Enter Telegram code: ")
                    code = code.strip()

                print("Signing in...")
                await client.sign_in(phone_number, code)
                print("Successfully signed in.")
            except SessionPasswordNeededError:
                password = await asyncio.to_thread(input, "Enter 2FA password: ")
                password = password.strip()
                await client.sign_in(password=password)
                print("Successfully signed in with 2FA.")
            except Exception as e:
                print(f"Authorization failed: {e}. Retrying...")
                continue

        await initialize_commands()

        print("Bot successfully started.")
        await client.run_until_disconnected()

    except Exception as e:
        print(f"Bot failed to start: {e}")


if __name__ == "__main__":
    client.loop.run_until_complete(main())
