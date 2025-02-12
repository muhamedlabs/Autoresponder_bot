import asyncio

async def auto_reply(event):
    """Автоответ на слово 'утро'."""
    await asyncio.sleep(5)
    await event.respond("Утро — это начало нового дня!")
    print(f"Ответ на 'утро' в чате {event.chat_id}")


