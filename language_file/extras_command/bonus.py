translations = {
    "triumphator_messages": {
        "ru": [
            "**Поздравляем тебя, Ронин! 🎉**\n\n"
            "Ты выиграл эксклюзивную возможность бесплатно прорекламироваться на наших проектах! 🚀 "
            "У тебя есть 24 часа, чтобы откликнуться. Не упусти шанс! 💪\n\n"
            "Кстати, не забудь посетить наш сайт: https://muhamedlabs.pro",  

            "**Ронин, ты победитель! 🏆**\n\n"
            "Твоя удача сегодня на высоте! 😎 Ты получаешь возможность бесплатной рекламы (видео или текстовой) "
            "на наших проектах! Ждём твой ответ в течение 24 часов! ⏳\n\n"
            "Кстати, не забудь заглянуть на наш сайт: https://muhamedlabs.pro",  

            "**Внимание, Ронин! Ты выиграл! 💥**\n\n"
            "Поздравляем с победой в розыгрыше! 🎊 У тебя есть 24 часа, чтобы забрать свой приз — "
            "бесплатную рекламу на наших площадках! Пиши скорее! 🚀\n\n"
            "Кстати, не забудь посетить наш сайт: https://muhamedlabs.pro",  

            "**Вот это везение, Ронин! 🔥**\n\n"
            "Ты стал победителем и теперь можешь получить свою бесплатную рекламу! 🏅 "
            "Напиши нам в течение 24 часов, чтобы активировать приз! ⏳\n\n"
            "Кстати, не забудь заглянуть на сайт: https://muhamedlabs.pro",  

            "**Ты в центре внимания, Ронин! 🏅**\n\n"
            "Твой выигрыш — бесплатная реклама на наших проектах! 💪 Не упусти возможность, "
            "у тебя 24 часа, чтобы откликнуться! 🚀\n\n"
            "Кстати, не забудь посетить наш сайт: https://muhamedlabs.pro",
        ],
        "uk": [
            "**Вітаємо тебе, Ронін! 🎉**\n\n"
            "Ти виграв ексклюзивну можливість безкоштовно прорекламуватися на наших проектах! 🚀 "
            "У тебе є 24 години, щоб відгукнутися. Не пропусти свій шанс! 💪\n\n"
            "До речі, не забудь завітати на наш сайт: https://muhamedlabs.pro",  

            "**Ронін, ти переможець! 🏆**\n\n"
            "Твоя удача сьогодні на висоті! 😎 Ти отримуєш можливість безкоштовної реклами (відео чи текстової) "
            "на наших проектах! Чекаємо на твою відповідь протягом 24 годин! ⏳\n\n"
            "До речі, не забудь заглянути на наш сайт: https://muhamedlabs.pro",  

            "**Увага, Ронін! Ти виграв! 💥**\n\n"
            "Вітаємо з перемогою у розіграші! 🎊 У тебе є 24 години, щоб забрати свій приз — "
            "безкоштовну рекламу на наших майданчиках! Пиши швидше! 🚀\n\n"
            "До речі, не забудь завітати на наш сайт: https://muhamedlabs.pro",  

            "**Оце везіння, Ронін! 🔥**\n\n"
            "Ти став переможцем і тепер можеш отримати свою безкоштовну рекламу! 🏅 "
            "Напиши нам протягом 24 годин, щоб активувати приз! ⏳\n\n"
            "До речі, не забудь заглянути на сайт: https://muhamedlabs.pro",  

            "**Ти в центрі уваги, Ронін! 🏅**\n\n"
            "Твій виграш — безкоштовна реклама на наших проектах! 💪 Не пропусти можливість, "
            "у тебе є 24 години, щоб відгукнутися! 🚀\n\n"
            "До речі, не забудь завітати на наш сайт: https://muhamedlabs.pro",
        ],
        "en": [
            "**Congratulations, Ronin! 🎉**\n\n"
            "You've won an exclusive opportunity to get free promotion on our projects! 🚀 "
            "You have 24 hours to respond. Don't miss your chance! 💪\n\n"
            "By the way, don't forget to visit our website: https://muhamedlabs.pro",  

            "**Ronin, you're a winner! 🏆**\n\n"
            "Your luck is on point today! 😎 You've earned a chance to get free promotion (video or text) "
            "on our projects! We're waiting for your response within 24 hours! ⏳\n\n"
            "By the way, don't forget to check out our website: https://muhamedlabs.pro",  

            "**Attention, Ronin! You've won! 💥**\n\n"
            "Congratulations on your victory in the giveaway! 🎊 You have 24 hours to claim your prize — "
            "free promotion on our platforms! Write to us soon! 🚀\n\n"
            "By the way, don't forget to visit our website: https://muhamedlabs.pro",  

            "**What a stroke of luck, Ronin! 🔥**\n\n"
            "You've become a winner and can now claim your free promotion! 🏅 "
            "Write to us within 24 hours to activate your prize! ⏳\n\n"
            "By the way, don't forget to check out our website: https://muhamedlabs.pro",  

            "**You're in the spotlight, Ronin! 🏅**\n\n"
            "Your prize is free promotion on our projects! 💪 Don't miss this opportunity, "
            "you have 24 hours to respond! 🚀\n\n"
            "By the way, don't forget to visit our website: https://muhamedlabs.pro",
        ]
    }
}


def get_translation(key, lang):
    """Получает перевод на нужном языке, если нет — использует русский."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])