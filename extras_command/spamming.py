import asyncio
from telethon import TelegramClient, events
from BANNED_FILES.config import GIF_URL, DELAY, MAX_LIMIT

async def spam_pro(client, chat_id, text, count):
    """Функция спама с гифкой"""
    for _ in range(count):
        try:
            await client.send_message(chat_id, message=text, file=GIF_URL)
            await asyncio.sleep(DELAY)
        except Exception:
            return False
    return True

def register_proces(client):
    """Регистрация обработчиков только для бота"""

    @client.on(events.NewMessage(pattern=r'(?i)СпамPro\s+(\d+)\s+(.+)\s*'))
    async def handler(event):
        # Проверяем что сообщение от самого бота
        if not event.out:
            return
            
        count = int(event.pattern_match.group(1))
        text = event.pattern_match.group(2).strip()

        if count > MAX_LIMIT:
            return

        await spam_pro(client, event.chat_id, text, count)