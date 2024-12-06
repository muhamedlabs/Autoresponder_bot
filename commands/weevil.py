async def handle_weevil(client, chat_id):
    await client.send_message(
        chat_id,
        "📢 **Добро пожаловать в Топ чат Тясицу!**\n\n"
        "Ты попал в место, где каждый найдет что-то для себя! Здесь ты можешь не только приятно пообщаться, но и узнать много интересного — "
        "получить полезные советы, обсудить новинки, найти единомышленников и просто провести время в компании хороших людей. 🌟\n\n"
        "Наш чат — это не просто место для общения, это целая комьюнити, где каждый участник важен. "
        "Мы всегда рады новым друзьям, и у нас всегда есть чем поделиться.\n\n"
        "Помимо этого, в чате тебя ждут регулярные обсуждения интересных тем, конкурсы, а также множество других активностей, "
        "которые сделают твое пребывание незабываемым.\n\n"
        "Так что не теряй времени и присоединяйся прямо сейчас! Нам есть о чём поговорить! 😉\n\n"
        "👉 [Залетай в чат Тясицу и становись частью нашей команды!](https://t.me/+QxnWNDp95wFhOWFi)",
        file="Фото_материал/Аватарка Тясицу copy.jpg",  # Замените путь на файл вашей картинки
        parse_mode="markdown"
    )
