import random
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError
from BANNED_FILES.config import RedisManager, BATTLE_GIF
from redis_storage.users_info import UsersInfo
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.battle import get_translation

redis = RedisManager()

async def load_chat_ids_from_redis():
    """Загружает все уникальные chat_id из Redis по UsersInfo."""
    chat_ids = set()
    async with redis:
        records = await redis.load_many(UsersInfo, key="*")
        for record in records:
            if record.chat_id:
                chat_ids.add(int(record.chat_id))
    return list(chat_ids)

async def send_battle_messages(client):
    """Отправляет сообщение о войне в 10 доступных чатах."""
    chat_ids = await load_chat_ids_from_redis()
    
    if not chat_ids:
        return

    if not BATTLE_GIF:
        return

    winners_sent = 0
    tried_chats = set()

    while winners_sent < 10 and len(tried_chats) < len(chat_ids):
        chat_id = random.choice(chat_ids)
        if chat_id in tried_chats:
            continue
        tried_chats.add(chat_id)

        try:
            entity = await client.get_entity(chat_id)

            # Ищем первого живого участника
            recipient_id = None
            async for user in client.iter_participants(entity):
                if not user.bot:
                    recipient_id = user.id
                    break

            if recipient_id is None:
                continue

            # Определяем язык пользователя
            lang = await get_user_language(recipient_id) or "ru"
            batl_messages = get_translation("battle_messages", lang)
            if not batl_messages or not isinstance(batl_messages, list):
                continue

            random_text = random.choice(batl_messages)
            await client.send_file(entity, BATTLE_GIF, caption=random_text)
            winners_sent += 1
            print(f"Команда 'СхваткаPro' : отправлено сообщение в чат {chat_id}")

        except (YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError):
            continue
        except Exception:
            continue

def register_proces(client):
    """Регистрирует триггер на команду 'СхваткаPro' для user-bot."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^СхваткаPro$"))
    async def check_battle_trigger(event):
        await send_battle_messages(client)
        