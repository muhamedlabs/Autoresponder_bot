import os
import random
from telethon import events

# Путь к гифке
GIF_PATH = os.path.abspath("Видео_материал/Gif/Vacation.gif")

# Рандомные тексты для ответа
VACATION_MESSAGES = [
   
   "**Отпуск начался! 🎉**\n\nЗабудь про будильники и дедлайны – теперь только отдых, расслабление и новые впечатления! Наслаждайся каждым моментом! 🌴☀️",  

   "**Свобода, БРО! 🚀**\n\nОставь заботы позади, впереди только отдых и приключения! Пусть отпуск будет незабываемым! 😎🔥",  

   "**Режим отдыха включён! 🏖️**\n\nВремя забыть про работу и полностью посвятить себя отдыху! Лови каждый миг удовольствия! 🍹",  

   "**Перезагрузка активирована! 🌍**\n\nПутешествуй, отдыхай, заряжайся! Пусть этот отпуск будет наполнен яркими моментами и крутыми эмоциями! ✈️💙",  

   "**Настоящий чилл! 🎶**\n\nСейчас только море, солнце, природа и полное расслабление! Лови волну позитива и наслаждайся! 🌊😌",  
] 

def register_auto_reply(client):
    """Регистрирует автоответ на слово 'отпуск'."""

    @client.on(events.NewMessage(outgoing=True))
    async def weekend_reply(event):
        if "отпуск" in event.message.text.lower():
            # Проверяем, что сообщение в личке
            if event.is_group or event.is_channel:
                return  # В группах не реагируем

            random_text = random.choice(VACATION_MESSAGES)

            if not os.path.exists(GIF_PATH):
                print(f"Ошибка: Файл гифки '{GIF_PATH}' не найден!")
                await event.respond(random_text)
                return

            await event.client.send_file(event.chat_id, GIF_PATH, caption=random_text)
            print(f"Sent a gif with a text for the vacation.")