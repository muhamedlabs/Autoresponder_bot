import os 
import random
import re
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError
from BANNED_FILES.config import FILE_NAME, BATTLE_GIF
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.battle import get_translation

# Функция загрузки списка чатов
def load_chat_ids():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()

    chat_ids = re.findall(r"ID чата: (\d+)", content)  # Извлекаем ID чатов
    return list(map(int, chat_ids))  # Преобразуем в список чисел

async def send_winner_messages(client):
    """Отправляет сообщение о войне в 10 случайных чатов."""
    chat_ids = load_chat_ids()
    
    if len(chat_ids) < 10:
        return  # Прекращаем, если чатов меньше 10

    selected_chats = random.sample(chat_ids, 10)  # Выбираем 10 случайных чатов

    if not os.path.exists(BATTLE_GIF):
        return  # Если нет гифки, ничего не делаем

    for chat_id in selected_chats:
        try:
            # Находим любого участника чата, кроме бота
            async for user in client.iter_participants(chat_id):
                if not user.bot:  # Берём первого живого участника
                    recipient_id = user.id
                    break
            else:
                continue  # Если нет участников, пропускаем чат

            # Получаем язык именно этого пользователя
            lang = get_user_language(recipient_id) or "ru"  
            batl_messages = get_translation("battle_messages", lang)

            if not batl_messages or not isinstance(batl_messages, list):
                continue  # Пропускаем, если нет перевода

            random_text = random.choice(batl_messages)  # Берём случайное сообщение
            
            await client.send_file(chat_id, BATTLE_GIF, caption=random_text)

        except (YouBlockedUserError, UserIsBlockedError, PeerIdInvalidError):
            continue  # Пропускаем недоступные чаты
        except Exception:
            continue  # Игнорируем любые другие ошибки

def register_proces(client):
    """Регистрирует триггер на команду 'СхваткаPro'."""
    
    @client.on(events.NewMessage(outgoing=True))
    async def check_raffle_trigger(event):
        """Запускает розыгрыш, если бот отправляет именно 'СхваткаPro' (с учётом регистра)."""
        if event.message.text.strip() == "СхваткаPro":  # Проверяем точное совпадение
            await send_winner_messages(client)