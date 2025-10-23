import random
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError
from BANNED_FILES.config import RedisManager, BONUS_GIF
from redis_storage.users_info import UsersInfo
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.bonus import get_translation

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


async def send_winner_messages(client):
    """Отправляет сообщение о выигрыше в 3 доступных чатах."""
    chat_ids = await load_chat_ids_from_redis()
    
    if not chat_ids or not BONUS_GIF:
        return

    winners_sent = 0
    tried_chats = set()

    while winners_sent < 3 and len(tried_chats) < len(chat_ids):
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
            win_messages = get_translation("bonus_messages", lang)
            if not win_messages or not isinstance(win_messages, list):
                continue

            random_text = random.choice(win_messages)
            await client.send_file(entity, BONUS_GIF, caption=random_text)
            winners_sent += 1
            print(f"[INFO] Команда 'РонинPro' : отправлено сообщение в чат {chat_id}")

        except (YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError):
            continue
        except Exception:
            continue


def register_proces(client):
    """Регистрирует триггер на команду 'РонинPro' для user-bot."""
    
    @client.on(events.NewMessage(outgoing=True, pattern=r"^РонинPro$"))
    async def check_raffle_trigger(event):
        await send_winner_messages(client)

