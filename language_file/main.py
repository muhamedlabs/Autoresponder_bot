translations = {
    "welcome": {
        "ru": "👹 **Путь начинается, воин!** Это автоматическое сообщение, "
                    "которое отправляется без покупки **Telegram Premium**. Мы больше не будем беспокоить вас, "
                    "так что пишите, что хотите узнать или приобрести, чтобы не забрать друг у друга время.\n\n"
                    "При использовании команд: `!info`, `!donate`, `!gift`, `!bots` авто-ответчик обязательно ответит на ваш запрос.\n\n"
                    "Также, вы можете посетить сайт **Андрея Мухамеда** для дополнительной информации: https://muhamedlabs.pro",

        "en": "👹 **The journey begins, warrior!** This is an automated message, "
                    "which is sent without the purchase of **Telegram Premium**. We won't bother you anymore, "
                    "so write what you want to learn or purchase so you don't take up each other's time. \n\n"
                    "When using the commands: `!info`, `!donate`, `!gift`, `!bots` the auto-responder will definitely answer your request.\n\n"
                    "Also, you can visit **Andrew Muhamed's** website for more information: https://muhamedlabs.pro",

        "uk": "👹 **Шлях починається, воїне!** Це автоматичне повідомлення, "
                    "яке надсилається без купівлі **Telegram Premium**. Ми більше не будемо турбувати вас, "
                    "тож пишіть, що хочете дізнатися або придбати, щоб не забрати один в одного час.\n\n"
                    "При використанні команд: `!info`, `!donate`, `!gift`, `!bots` авто-відповідач обов`язково відповість на ваш запит.\n\n"
                    "Також, ви можете відвідати сайт **Андрія Мухамеда** для додаткової інформації: https://muhamedlabs.pro"
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский
