from telethon import events 
import asyncio

# Запрещённые слова (с учётом регистра)
FORBIDDEN_WORDS = ["УтроPro", "НочьPro", "РаботаPro", "ТиражPro", "РонинPro", "ПесняPro", "ДамойPro", "ВиходнойPro", "ОтпускPro", "ХелпPro"]

def register_auto_delete(client):
    """Регистрирует авто-удаление сообщений бота у себя и у пользователей."""
    
    @client.on(events.NewMessage(outgoing=True))  # Удаляем только свои сообщения
    async def auto_delete_handler(event):
        if not event.message.text:
            return  # Игнорируем пустые сообщения
        
        text = event.message.text  # Оставляем регистр

        # Проверяем точное совпадение с запрещёнными словами
        if any(word in text for word in FORBIDDEN_WORDS):
            await asyncio.sleep(45)  # Ждём 45 секунд
            
            try:
                # Удаляем сообщение у всех, если это возможно
                await client.delete_messages(event.chat_id, event.message.id, revoke=True)
                print(f"Chat message deleted {event.chat_id}: {text}")
            except Exception as e:
                print(f"Ошибка удаления: {e}")