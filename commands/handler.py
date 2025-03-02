# Файл является основным обработчиком команд

from BANNED_FILES.config import PHOTO_handlerRU, PHOTO_handlerUK, PHOTO_handlerEN
from language_file.UserLanguage import get_user_language
from language_file.handler import get_translation

from commands.info import handle_info
from commands.gift import handle_gift
from commands.bots import handle_bots
from commands.donate import handle_donate
from commands.advertising import handle_advertising
from commands.news import handle_news
from commands.podcast import handle_podcast
from commands.quotes import handle_quotes
from commands.picture import handle_picture
from commands.faq import handle_faq
from commands.weevil import handle_weevil



# Функция для обработки команд
async def handle_command(client, chat_id, user_id, command, message_text):
    ignored_commands = {"!start", "!skip", "!ignore"}
    
    if command in ignored_commands:
        # Игнорируем указанные команды
        return
    
    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Словарь соответствий языков и изображений
    photo_dict = {
        "ru": PHOTO_handlerRU,
        "uk": PHOTO_handlerUK,
        "en": PHOTO_handlerEN
    }

    # Выбираем нужное фото, если язык неизвестен — используем дефолтное
    PHOTO_handler = photo_dict.get(lang, PHOTO_handlerRU)
    
    if command == "!info":
        await handle_info(client, chat_id, user_id, message_text)
    elif command == "!gift":
        await handle_gift(client, chat_id, user_id, message_text)
    elif command == "!bots":
        await handle_bots(client, chat_id, user_id, message_text)
    elif command == "!donate":
        await handle_donate(client, chat_id, user_id, message_text)
    elif command == "!advertising":
        await handle_advertising(client, chat_id, user_id, message_text)
    elif command == "!news":
        await handle_news(client, chat_id, user_id, message_text)  
    elif command == "!podcast":
        await handle_podcast(client, chat_id, user_id, message_text)
    elif command == "!quote":
        await handle_quotes(client, chat_id, user_id, message_text)
    elif command == "!picture":
        await handle_picture(client, chat_id, user_id, message_text)
    elif command == "!faq":
        await handle_faq(client, chat_id, user_id, message_text)
    elif command == "!tyasitsu":
        await handle_weevil(client, chat_id, user_id, message_text)              
    else:
        # Если команда неизвестна, отправляем красивое сообщение и изображение
        await client.send_message(
            chat_id,
            get_translation("unknown", lang),
            file=PHOTO_handler  # Укажите ваше изображения
        )