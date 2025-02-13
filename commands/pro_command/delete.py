from telethon import events
import asyncio

FORBIDDEN_WORDS = ["утро", "ночь", "работа", "тираж"]

def register_auto_delete(client):
    """Регистрирует авто-удаление сообщений бота у себя и у пользователей."""
    
    @client.on(events.NewMessage(outgoing=True))  # Удаляем только свои сообщения
    async def auto_delete_handler(event):
        if not event.message.text:
            return  # Игнорируем пустые сообщения
        
        text = event.message.text.lower()

        # Проверяем, содержит ли сообщение запрещённые слова
        if any(word in text for word in FORBIDDEN_WORDS):
            await asyncio.sleep(30)  # Ждём 30 секунд
            
            try:
                # Удаляем сообщение у всех, если это возможно
                await client.delete_messages(event.chat_id, event.message.id, revoke=True)
                print(f"Chat message deleted {event.chat_id}: {text}")
            except Exception as e:
                print(f"Ошибка удаления: {e}")
