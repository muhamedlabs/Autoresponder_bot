import asyncio 
import random
from telethon import events
from language_file.transcribation.MemberLanguage import get_user_language
from language_file.extras_command.help import get_translation

def register_proces(client):
    """Регистрирует команду 'ХелпPro'."""

    @client.on(events.NewMessage(outgoing=True, pattern=r"^ХелпPro$"))
    async def help_command(event):
        """Отправляет сообщение на языке получателя и удаляет его через 3–5 минут."""
        try:
            # Определяем язык пользователя, которому бот пишет
            user_id = event.chat_id
            lang = get_user_language(user_id)

            # Получаем перевод
            help_message = get_translation("help_messages", lang)

            # Отправляем сообщение и сохраняем его объект
            sent_message = await event.respond(help_message)

            # Случайная задержка перед удалением (3–5 минут)
            delay = random.randint(180, 300)  # 180–300 секунд (3–5 мин)
            await asyncio.sleep(delay)

            # Удаляем оба сообщения (команду и ответ бота)
            await event.delete()  # Удаляет сообщение с командой "ХелпPro"
            await sent_message.delete()  # Удаляет ответ бота

        except Exception as e:
            print(f"[ERROR] Ошибка при отправке или удалении сообщения: {e}")