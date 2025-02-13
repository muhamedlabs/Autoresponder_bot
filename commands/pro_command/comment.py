import os
from telethon import events

COMMENT_FILE = "Ignore/User_comments.txt"  # Файл для хранения комментариев

async def save_comment(user_id, username, first_name, last_name, comment):
    """Сохраняет комментарий в файл."""
    user_link = f"https://t.me/{username}" if username else "Нет юзернейма"
    first_name = first_name or "Нет"
    last_name = last_name or "Нет"

    entry = (
        f"ID пользователя: {user_id}\n"
        f"Ссылка: {user_link}\n"
        f"Имя: {first_name}\n"
        f"Фамилия: {last_name}\n"
        f"Комментарий: {comment}\n"
        f"{'-' * 40}\n"
    )

    # Создаем файл, если его нет, и добавляем запись
    with open(COMMENT_FILE, "a", encoding="utf-8") as file:
        file.write(entry)

    print(f"Комментарий сохранён для {user_id}")

def register_comment_handler(client):
    """Регистрирует команду /comment."""
    
    @client.on(events.NewMessage(pattern=r"^/comment\s+(.+)", incoming=True))
    async def handle_comment(event):
        """Обрабатывает команду /comment <текст>, но только в ЛС с ботом."""
        if event.is_group or event.is_channel:
            await event.reply("❌ Команда /comment доступна только в ЛИЧНЫХ сообщениях с ботом.")
            return

        user = await event.get_sender()  # Получаем данные пользователя
        comment = event.pattern_match.group(1).strip()

        if not user:
            await event.reply("❌ Ошибка: Не удалось получить информацию о пользователе.")
            return

        user_id = user.id
        username = user.username
        first_name = user.first_name
        last_name = user.last_name

        await save_comment(user_id, username, first_name, last_name, comment)
        await event.reply("✅ Ваш комментарий сохранён и когда-нибудь появится на сайте!")
