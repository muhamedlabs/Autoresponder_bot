import asyncio
import os
from datetime import datetime, timedelta
from telethon.errors import YouBlockedUserError
from BANNED_FILES.config import RedisManager, VIDEO_FILE
from redis_storage.users_info import UsersInfo
from language_file.transcribation.UserLanguage import get_user_language
from language_file.main import get_translation

# Инициализация Redis
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

async def register_proces(user_id: str, proces_type: str, data: dict = None):
    """Регистрирует процесс для пользователя в Redis"""
    if data is None:
        data = {}
    
    async with redis:
        user_record = await redis.load(UsersInfo, key=str(user_id))
        
        if user_record:
            user_record.proces_type = proces_type
            user_record.proces_data = data
            user_record.proces_started = get_ukraine_time().isoformat()
            user_record.last_activity = get_ukraine_time().isoformat()
            
            await redis.save(user_record, key=str(user_id))
            print(f"[Redis] Процесс '{proces_type}' зарегистрирован для пользователя {user_id}")
        else:
            user_record = UsersInfo(
                user_id=str(user_id),
                proces_type=proces_type,
                proces_data=data,
                proces_started=get_ukraine_time().isoformat(),
                last_activity=get_ukraine_time().isoformat(),
                timestamp=get_ukraine_time().isoformat()
            )
            await redis.save(user_record, key=str(user_id))
            print(f"[Redis] Создана новая запись с процессом '{proces_type}' для пользователя {user_id}")

# === Функции обработки пользователя ===
async def extract_user_info(event, client):
    """Извлекает информацию о пользователе из события"""
    sender = await event.get_sender()
    if sender is None:
        print("Ошибка: Не удалось получить отправителя.")
        return None
    
    user_info = {
        'user_id': str(sender.id),
        'chat_id': event.chat_id,
        'phone': sender.phone if sender.phone else "No phone number",
        'username': sender.username if sender.username else "None",
        'first_name': sender.first_name if sender.first_name else "None",
        'last_name': sender.last_name if sender.last_name else "None",
        'link': f"https://t.me/{sender.username}" if sender.username != "None" else "No link",
        'message_text': event.message.text.strip() if event.message.text else "",
    }
    
    # Определяем язык пользователя
    user_info['lang'] = await get_user_language(client, user_info['user_id'], user_info['message_text'])
    user_info['message_text_lower'] = user_info['message_text'].lower()
    
    return user_info

async def handle_welcome_message(client, user_info, is_reset=False):
    """Отправляет приветственное сообщение пользователю"""
    try:
        if os.path.exists(VIDEO_FILE):
            await client.send_file(
                user_info['chat_id'],
                VIDEO_FILE,
                caption=get_translation("welcome", user_info['lang'])
            )
        else:
            await client.send_message(
                user_info['chat_id'],
                get_translation("welcome", user_info['lang'])
            )

        await save_replied_user(
            user_id=user_info['user_id'],
            username=user_info['username'],
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],
            phone=user_info['phone'],
            chat_id=user_info['chat_id'],
            link=user_info['link']
        )
        
        log_msg = f"Приветствие отправлено пользователю {user_info['user_id']}"
        if is_reset:
            log_msg = f"[INFO] Приветствие отправлено пользователю {user_info['user_id']} после команды !start"
        print(log_msg)
        
        return True
        
    except YouBlockedUserError:
        print(f"{'[WARN]' if is_reset else ''} Пользователь {user_info['user_id']} заблокировал бота.")
        return False
    except Exception as e:
        print(f"Не удалось отправить приветственное сообщение: {e}")
        return False

async def handle_user_reset(user_id: str):
    """Обрабатывает сброс пользователя"""
    await remove_user_from_redis(user_id)
    user_locks.pop(user_id, None)

def is_user_locked(user_id: str) -> bool:
    """Проверяет, есть ли активная лока у пользователя"""
    return user_locks.get(user_id, False)