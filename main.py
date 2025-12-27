import os
import asyncio
from datetime import datetime, timedelta

from telethon import TelegramClient, events
from telethon.errors import YouBlockedUserError, SessionPasswordNeededError

from BANNED_FILES.config import phone_number, api_hash, api_id, VIDEO_FILE, RedisManager
from commands.UserHandler import handle_command  # Загрузка основных команд
from language_file.transcribation.UserLanguage import get_user_language  # Загрузка определения языка
from extras_command.UserProces import load_proces  # Загрузка доп команд
from extras_command.UserRemover import load_remover  # Загрузка автоудаления команд
from extras_command.UserNotes import load_сomment  # Загрузка комментариев от пользователей
from language_file.main import get_translation  # Загрузка транскрипции
from extras_command.ads_command import load_ads_command  # Загрузка архиватора
from redis_storage.users_info import UsersInfo 

# Инициализация клиента и Redis
client = TelegramClient("session_name", api_id, api_hash)
redis = RedisManager()

# Локи пользователей для защиты от спама
user_locks = {}
LOCK_EXPIRATION = 10  # Время жизни локи в секундах

# === Функции работы с Redis ===
async def has_replied(user_id: str) -> bool:
    """Проверяет, есть ли пользователь в Redis (в таблице UsersInfo)"""
    async with redis:
        record = await redis.load(UsersInfo, key=str(user_id))
        return record is not None

async def save_replied_user(user_id: str, **kwargs):
    """Сохраняет данные пользователя в Redis (UsersInfo)"""
    async with redis:
        user_record = UsersInfo(
            user_id=str(user_id),
            timestamp=get_ukraine_time().isoformat(),
            **kwargs
        )
        await redis.save(user_record, key=str(user_id))
        print(f"Пользователь {user_id} сохранён в Redis (UsersInfo)")

async def remove_user_from_redis(user_id: str):
    """Удаляет пользователя из Redis (UsersInfo)"""
    async with redis:
        await redis.delete(UsersInfo, key=str(user_id))

# === Время по Украине ===
def get_ukraine_time():
    """Возвращает текущее время по Украине (UTC+3)"""
    return datetime.utcnow() + timedelta(hours=3)

# === Локи для защиты от спама ===
async def set_user_lock(user_id: str):
    """Устанавливает локу для пользователя на время LOCK_EXPIRATION"""
    user_locks[user_id] = True
    await asyncio.sleep(LOCK_EXPIRATION)
    user_locks.pop(user_id, None)

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

    message_text = event.message.text.strip() if event.message.text else ""
    message_text_lower = message_text.lower()

    # Определяем язык пользователя (ваша функция работает с оригинальным текстом)
    lang = await get_user_language(client, user_id, message_text)

    # === Команда сброса статуса (!start) ===
    if message_text_lower == "!start":
        await remove_user_from_redis(user_id)
        user_locks.pop(user_id, None)
        
        # Отправляем приветствие после сброса
        try:
            if os.path.exists(VIDEO_FILE):
                await client.send_file(
                    chat_id,
                    VIDEO_FILE,
                    caption=get_translation("welcome", lang)
                )
            else:
                await event.reply(get_translation("welcome", lang))

            await save_replied_user(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                chat_id=chat_id,
                link=link
            )
            print(f"[INFO] Приветствие отправлено пользователю {user_id} после команды !start")
            
        except YouBlockedUserError:
            print(f"[WARN] Пользователь {user_id} заблокировал бота.")
        except Exception as e:
            print(f"Не удалось отправить приветственное сообщение: {e}")
        return

    # === Если есть активная лока — игнорируем спам ===
    if user_locks.get(user_id):
        return

    # Устанавливаем локу для текущего пользователя
    asyncio.create_task(set_user_lock(user_id))

    # === Отправляем приветствие только если пользователь новый (нет в Redis) ===
    if not await has_replied(user_id):
        try:
            if os.path.exists(VIDEO_FILE):
                await client.send_file(
                    chat_id,
                    VIDEO_FILE,
                    caption=get_translation("welcome", lang)
                )
            else:
                await event.reply(get_translation("welcome", lang))

            await save_replied_user(
                user_id=user_id,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                chat_id=chat_id,
                link=link
            )
            print(f"Приветствие отправлено пользователю {user_id}")
            
        except YouBlockedUserError:
            print(f"Пользователь {user_id} заблокировал бота.")
        except Exception as e:
            print(f"Не удалось отправить приветственное сообщение: {e}")

    # === Обработка команд ===
    if message_text_lower.startswith("!"):
        command = message_text_lower.split()[0]
        await handle_command(client, chat_id, user_id, command, message_text_lower)


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
