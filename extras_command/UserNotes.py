import os
import asyncio
from telethon import events
from BANNED_FILES.config import COMMENTS_FILE, COMMENTS_IMAGE
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.notes import get_translation


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
    with open(COMMENTS_FILE, "a", encoding="utf-8") as file:
        file.write(entry)




def load_сomment(client):
    """Регистрирует команду /comment."""
    
    @client.on(events.NewMessage(pattern=r"^/comment\s+(.+)", incoming=True))
    async def handle_comment(event):
        """Обрабатывает команду /comment <текст>, но только в ЛС с ботом."""
        if event.is_group or event.is_channel:
            await event.reply("Команда /comment доступна только в ЛИЧНЫХ сообщениях с ботом.", reply_to=event.message.id)
            return

        user = await event.get_sender()  # Получаем данные пользователя
        comment = event.pattern_match.group(1).strip()

        if not user:
            await event.reply("Ошибка: Не удалось получить информацию о пользователе.", reply_to=event.message.id)
            return

        user_id = user.id
        username = user.username
        first_name = user.first_name
        last_name = user.last_name

        await save_comment(user_id, username, first_name, last_name, comment)

        # Определяем язык пользователя
        lang = get_user_language(user_id) or "ru"
        reply_text = get_translation("comment_response", lang)

        # Ожидание 5 минут перед отправкой ответа
        await asyncio.sleep(300)  # 300 секунд = 5 минут

        # Отправка ответа на сообщение пользователя
        if os.path.exists(COMMENTS_IMAGE):
            await event.reply(reply_text, file=COMMENTS_IMAGE, reply_to=event.message.id)
        else:
            await event.reply(reply_text, reply_to=event.message.id)