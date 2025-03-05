import random
from language_file.UserLanguage import get_user_language
from language_file.quotes import get_translation



async def handle_quotes(client, chat_id, user_id, message_text):

    # Определяем язык пользователя (оптимизировано)
    lang = await get_user_language(client, user_id, message_text)

    # Случайный выбор цитаты
    random_quote = random.choice(get_translation("quotes", lang))

    # Отправка цитаты
    await client.send_message(chat_id, random_quote)