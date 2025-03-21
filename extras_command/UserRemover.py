from telethon import events 
import asyncio
from BANNED_FILES.config import FORBIDDEN_WORDS

def load_remover(client):
    """Регистрирует авто-удаление сообщений бота у себя и у пользователей."""
    
    @client.on(events.NewMessage(outgoing=True))  # Удаляем только свои сообщения
    async def auto_delete_handler(event):
        if not event.message.text:
            return  # Игнорируем пустые сообщения
        
        text = event.message.text  # Оставляем регистр

        # Проверяем точное совпадение с запрещёнными словами
        if any(word in text for word in FORBIDDEN_WORDS):
            await asyncio.sleep(5)  # Ждём 5 секунд
            
            try:
                # Удаляем сообщение у всех, если это возможно
                await client.delete_messages(event.chat_id, event.message.id, revoke=True)
            except Exception as e:
                print(f"Ошибка удаления: {e}")