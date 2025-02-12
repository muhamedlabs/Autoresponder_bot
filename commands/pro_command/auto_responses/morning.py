import asyncio

async def auto_reply(event):
    """Автоответ на слово 'утро'."""
    await asyncio.sleep(5)
    await event.respond("Доброе утро! ☀️")

