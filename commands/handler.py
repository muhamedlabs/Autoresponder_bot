# Файл является основным обработчиком команд

from commands.info import handle_info
from commands.gift import handle_gift
from commands.bots import handle_bots
from commands.donate import handle_donate
from commands.advertising import handle_advertising
from commands.news import handle_news
from commands.podcast import handle_podcast
from commands.quotes import handle_quotes
from commands.picture import handle_picture
from commands.faq import handle_faq
from commands.weevil import handle_weevil

# Функция для обработки команд
async def handle_command(client, chat_id, command):
    ignored_commands = {"!старт", "!пропуск", "!игнор"}
    
    if command in ignored_commands:
        # Игнорируем указанные команды
        return
    
    if command == "!инфо":
        await handle_info(client, chat_id)
    elif command == "!подарок":
        await handle_gift(client, chat_id)
    elif command == "!боты":
        await handle_bots(client, chat_id)
    elif command == "!донат":
        await handle_donate(client, chat_id)
    elif command == "!реклама":
        await handle_advertising(client, chat_id)
    elif command == "!новости":
        await handle_news(client, chat_id)  
    elif command == "!подкаст":
        await handle_podcast(client, chat_id)
    elif command == "!цитата":
        await handle_quotes(client, chat_id)
    elif command == "!картинка":
        await handle_picture(client, chat_id)
    elif command == "!чаво":
        await handle_faq(client, chat_id)
    elif command == "!тясицу":
        await handle_weevil(client, chat_id)              
    else:
        # Если команда неизвестна, отправляем красивое сообщение и изображение
        await client.send_message(
            chat_id,
            (
                "📢 **Неизвестная команда**\n"
                "Проверьте полный список доступных команд сервиса:\n\n"
                "`!инфо` — Информация о создателе и многом другом.\n"
                "`!тясицу` — Уникальный чат для поклонников создателя.\n"
                "`!подарок` — Специальные предложения для вас!\n"
                "`!новости` — Новые обновления от Мухамеда.\n" 
                "`!старт` — Перезапуск мини-бота user.\n"
                "`!реклама` — Узнать о наших рекламных услугах.\n"
                "`!донат` — Поддержите нас и помогите развивать проекты.\n"
                "`!чаво` — Популярные вопросы и ответы.\n"
                "`!цитата` — Мудрые высказывания великих людей.\n"
                "`!картинка` — Удивительные моменты от сервера Unsplash.\n"
                "`!подкаст` — Запись идеи самого создателя.\n"
                "`!боты` — Все боты разработаны командой Muhamed IT Solutions.\n"
                "`/comment текст` — Написать отзыв о Videoeditor, Creator, Designer, SS...\n\n"
                "🎯 Если вам нужна помощь, просто подождите, я скоро вам напишу!"
            ),
            file="Фото_материал/0.12 copy.png"  # Укажите путь к вашему изображению
        )

