translations = {
    "battle_messages": {
        "ru": [
            "**Война уже началась! ⚔️**\n\n"
            "Твоя система под угрозой! 🚨 Чтобы защитить её, срочно подпишись на наши проекты и заходи на сайт: https://muhamedlabs.pro",  

            "**Тревога! Твоя система атакована! 🚨**\n\n"
            "Враг уже здесь! 🛡️ Чтобы защитить свои данные, подпишись на наши проекты и переходи на сайт: https://muhamedlabs.pro",  

            "**Кибератака началась! 💻🔥**\n\n"
            "Твоя система в опасности! 🚨 Единственный способ защитить её — подписаться на наши проекты. Спасайся тут: https://muhamedlabs.pro",  

            "**Внимание! Твоя система под угрозой! 🚨**\n\n"
            "Враг уже в сети! ⚔️ Чтобы остановить его, подпишись на наши проекты и заходи на сайт: https://muhamedlabs.pro",  

            "**Твоя система взломана! 💀**\n\n"
            "Но ещё не всё потеряно! 🛡️ Подпишись на наши проекты, чтобы восстановить защиту: https://muhamedlabs.pro"
        ],
        "uk": [
            "**Війна вже почалася! ⚔️**\n\n"
            "Твоя система під загрозою! 🚨 Щоб захистити її, терміново підпишись на наші проекти та заходь на сайт: https://muhamedlabs.pro",  

            "**Тривога! Твою систему атаковано! 🚨**\n\n"
            "Ворог уже тут! 🛡️ Щоб захистити свої дані, підпишись на наші проекти та переходь на сайт: https://muhamedlabs.pro",  

            "**Кібератака розпочалася! 💻🔥**\n\n"
            "Твоя система в небезпеці! 🚨 Єдиний спосіб захистити її — підписатися на наші проекти. Рятуйся тут: https://muhamedlabs.pro",  

            "**Увага! Твоя система під загрозою! 🚨**\n\n"
            "Ворог уже в мережі! ⚔️ Щоб зупинити його, підпишись на наші проекти та заходь на сайт: https://muhamedlabs.pro",  

            "**Твою систему зламано! 💀**\n\n"
            "Але ще не все втрачено! 🛡️ Підпишись на наші проекти, щоб відновити захист: https://muhamedlabs.pro"
        ],
        "en": [
            "**The war has already begun! ⚔️**\n\n"
            "Your system is under threat! 🚨 To protect it, urgently subscribe to our projects and visit the website: https://muhamedlabs.pro",  

            "**Alert! Your system has been attacked! 🚨**\n\n"
            "The enemy is already here! 🛡️ To protect your data, subscribe to our projects and go to the website: https://muhamedlabs.pro",  

            "**A cyberattack has begun! 💻🔥**\n\n"
            "Your system is in danger! 🚨 The only way to protect it is to subscribe to our projects. Save yourself here: https://muhamedlabs.pro",  

            "**Attention! Your system is under threat! 🚨**\n\n"
            "The enemy is already in the network! ⚔️ To stop them, subscribe to our projects and visit the website: https://muhamedlabs.pro",  

            "**Your system has been hacked! 💀**\n\n"
            "But all is not lost! 🛡️ Subscribe to our projects to restore protection: https://muhamedlabs.pro"
        ]
    }
}


def get_translation(key, lang):
    """Получает перевод на нужном языке, если нет — использует русский."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])