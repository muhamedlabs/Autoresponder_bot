from telethon import events
import asyncio

def register_auto_delete(client, user_id):
    """Регистрирует авто-удаление сообщений с определёнными словами."""
    
    @client.on(events.NewMessage(outgoing=True))  # Удаляем только исходящие сообщения
    async def auto_delete_handler(event):
        if not event.message.text:
            return  # Игнорируем пустые сообщения
        
        text = event.message.text.lower()

        # Проверяем, содержит ли сообщение запрещённые слова
        if any(word in text for word in ["утро", "ночь", "работа"]):
            await asyncio.sleep(15)  # Ждём 15 секунд
            
            try:
                await client.delete_messages(event.chat_id, event.message.id)
                print(f"Удалено сообщение от {user_id}: {text}")
            except Exception as e:
                print(f"Ошибка удаления: {e}")


