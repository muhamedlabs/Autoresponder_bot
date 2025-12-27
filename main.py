import os
import asyncio
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError

from BANNED_FILES.config import phone_number, api_hash, api_id
from commands.UserHandler import handle_command  # Загрузка основных команд
from extras_command.UserProces import load_proces  # Загрузка доп команд
from extras_command.UserRemover import load_remover  # Загрузка автоудаления команд
from extras_command.UserNotes import load_сomment  # Загрузка комментариев от пользователей
from extras_command.ads_command import load_ads_command # Загрузка архиватора
from commands.start import extract_user_info, handle_welcome_message, handle_user_reset, is_user_locked, set_user_lock, has_replied, user_locks # Загрузка Redis протокола для старта

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

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    """Основной обработчик входящих сообщений"""
    if not event.is_private:
        return

    # Извлекаем информацию о пользователе
    user_info = await extract_user_info(event, client)
    if not user_info:
        return

    # === Команда сброса статуса (!start) ===
    if user_info['message_text_lower'] == "!start":
        await handle_user_reset(user_info['user_id'])
        await handle_welcome_message(client, user_info, is_reset=True)
        return

    # === Если есть активная лока — игнорируем спам ===
    if is_user_locked(user_info['user_id']):
        return

    # Устанавливаем локу для текущего пользователя
    asyncio.create_task(set_user_lock(user_info['user_id']))

    # === Отправляем приветствие только если пользователь новый (нет в Redis) ===
    if not await has_replied(user_info['user_id']):
        await handle_welcome_message(client, user_info, is_reset=False)

    # === Обработка команд ===
    if user_info['message_text_lower'].startswith("!"):
        command = user_info['message_text_lower'].split()[0]
        await handle_command(client, user_info['chat_id'], user_info['user_id'], 
                           command, user_info['message_text_lower'])

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
                    os.remove(code_file)
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
