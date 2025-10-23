import os 
import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient, events
from telethon.errors import YouBlockedUserError

from BANNED_FILES.config import phone_number, api_hash, api_id, VIDEO_FILE, RedisManager
from commands.UserHandler import handle_command # Загрузка основных команд
from language_file.transcribation.UserLanguage import get_user_language # Загрузка определения языка
from extras_command.UserProces import load_proces  # Загрузка доп команд
from extras_command.UserRemover import load_remover  # Загрузка автоудаления команд
from extras_command.UserNotes import load_сomment  # Загрузка комментариев от пользователей
from language_file.main import get_translation  # Загрузка транскрипции
from extras_command.ads_command import load_ads_command # Загрузка архиватора
from redis_storage.users_info import UsersInfo  # Класс данных UsersInfo

# === Инициализация клиента и Redis ===
client = TelegramClient('session_name', api_id, api_hash)
redis = RedisManager()

# === Локи пользователей для защиты от спама ===
user_locks = {}
LOCK_EXPIRATION = 10  # Время жизни локи в секундах

# === Время по Украине ===
def get_ukraine_time():
    return datetime.utcnow() + timedelta(hours=3)  # UTC+3

# === Функции работы с Redis ===
async def has_replied(user_id: str) -> bool:
    async with redis:
        record = await redis.load(UsersInfo, key=str(user_id))
        return record is not None

async def save_replied_user(user_id: str, **kwargs):
    async with redis:
        user_record = UsersInfo(
            user_id=str(user_id),
            timestamp=get_ukraine_time().isoformat(),
            **kwargs
        )
        await redis.save(user_record, key=str(user_id))
        print(f"Пользователь {user_id} сохранён")

async def remove_user_from_redis(user_id: str):
    async with redis:
        await redis.delete(UsersInfo, key=str(user_id))

# === Локи для защиты от спама ===
async def set_user_lock(user_id: str):
    user_locks[user_id] = True
    await asyncio.sleep(LOCK_EXPIRATION)
    user_locks.pop(user_id, None)

# === Инициализация всех команд бота ===
async def initialize_commands():

    # Подключение архиватора
    await load_ads_command(client)

     # Подключение автоудаления команд
    load_remover(client)

    # Подключение доп команд
    load_proces(client)

    # Подключение комментариев от пользователей
    load_сomment(client)

# === Основной обработчик сообщений ===
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return

    sender = await event.get_sender()
    if not sender:
        return

    user_id = str(sender.id)
    chat_id = event.chat_id
    phone = getattr(sender, "phone", None)
    username = getattr(sender, "username", None)
    first_name = getattr(sender, "first_name", None)
    last_name = getattr(sender, "last_name", None)
    link = f"https://t.me/{username}" if username else None

    message_text = event.message.text.strip().lower() if event.message.text else ""
    lang = await get_user_language(client, user_id, message_text)

    # === Команда сброса статуса (!start) ===
    if message_text == "!start":
        await remove_user_from_redis(user_id)
        user_locks.pop(user_id, None)
        # Отправляем приветствие после сброса
        try:
            if os.path.exists(VIDEO_FILE):
                await client.send_file(chat_id, VIDEO_FILE, caption=get_translation("welcome", lang))
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
                await client.send_file(chat_id, VIDEO_FILE, caption=get_translation("welcome", lang))
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

    # === Обработка команд ===
    if message_text.startswith("!"):
        command = message_text.split()[0]
        await handle_command(client, chat_id, user_id, command, message_text)

# === Запуск бота ===
async def main():
    try:
        await client.start(phone=lambda: phone_number)
        if not await client.is_user_authorized():
            password = input("Enter the two-factor authentication password: ")
            await client.start(password=password)

        await initialize_commands()
        print("Bot successfully started.")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"[Bot failed to start: {e}")

if __name__ == "__main__":
    asyncio.run(main())
