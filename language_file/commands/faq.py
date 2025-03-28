translations = {
  "queries": {
        "ru": "**❓ Часто задаваемые вопросы (FAQ) ❓**\n"
                "Здесь собраны ответы на популярные вопросы. Если не нашли нужное, напишите нам!\n\n"
                "**🔖 Какие услуги вы предоставляете?**\n"
                "Мы занимаемся продвижением рекламы, разработкой сайтов, Discord- и Telegram-ботов, их хостингом. Также создаем дизайнерские решения: аватарки, шапки каналов, посты и видеомонтаж.\n\n"
                "**🔖 Как заказать рекламу?**\n"
                "Заказ выполняется вручную. Цены смотрите через `!advertising`. [Больше подробносте на сайте!](https://muhamedlabs.pro)\n\n"
                "**🔖 Какие гарантии вы предоставляете?**\n"
                "Гарантируем качество, сроки и конфиденциальность данных.\n\n"
                "**🔖 Как поддержать ваши проекты?**\n"
                "Используйте команду `!donate`. Мы ценим вашу поддержку!\n\n"
                "**🔖 Какими проектами владеет Андрей Мухамед?**\n"
                "**Game Quest**, **Nanson**, **ANIME INDUSTRY**, **KINO INDUSTRY**, **Стримус**.\n\n"
                "**🔖 Как стать частью команды?**\n"
                "Мы открыты для талантливых людей! Пишите нам.\n\n"
                "**🔖 Где найти ваш контент?**\n"
                "На Telegram, YouTube и других платформах. Ссылки на все проекты [тут](https://muhamedlabs.pro)\n\n"
                "**📜 Остались вопросы?**\n"
                "Напишите нам! Ваше удовлетворение — наша цель.",

        "en": "**❓ Frequently Asked Questions (FAQ) ❓**\n"
                "Here are answers to popular questions. If you don't find what you're looking for, contact us!\n\n"
                "**🔖 What services do you provide?**\n"
                "We specialize in advertising promotion, website development, Discord and Telegram bots, hosting, and design solutions: avatars, channel headers, posts, and video editing.\n\n"
                "**🔖 How to order advertising?**\n"
                "Orders are processed manually. Check prices using `!advertising`. [More details on our website!](https://muhamedlabs.pro)\n\n"
                "**🔖 What guarantees do you provide?**\n"
                "We guarantee quality, deadlines, and data confidentiality.\n\n"
                "**🔖 How to support your projects?**\n"
                "Use the `!donate` command. We appreciate your support!\n\n"
                "**🔖 What projects does Andrey Muhamed own?**\n"
                "**Game Quest**, **Nanson**, **ANIME INDUSTRY**, **KINO INDUSTRY**, **Стримус**.\n\n"
                "**🔖 How to join the team?**\n"
                "We are open to talented people! Write to us.\n\n"
                "**🔖 Where can I find your content?**\n"
                "On Telegram, YouTube, and other platforms. Links to all projects are [here](https://muhamedlabs.pro)\n\n"
                "**📜 Still have questions?**\n"
                "Contact us! Your satisfaction is our goal.",

        "uk": "**❓ Часті питання (FAQ) ❓**\n"
                "Тут зібрані відповіді на популярні питання. Якщо не знайшли потрібне, напишіть нам!\n\n"
                "**🔖 Які послуги ви надаєте?**\n"
                "Ми займаємося просуванням реклами, розробкою сайтів, Discord- та Telegram-ботів, їхнім хостингом. Також створюємо дизайнерські рішення: аватарки, шапки каналів, пости та відеомонтаж.\n\n"
                "**🔖 Як замовити рекламу?**\n"
                "Замовлення виконується вручну. Ціни дивіться через `!advertising`. [Більше деталей на сайті!](https://muhamedlabs.pro)\n\n"
                "**🔖 Які гарантії ви надаєте?**\n"
                "Гарантуємо якість, терміни та конфіденційність даних.\n\n"
                "**🔖 Як підтримати ваші проекти?**\n"
                "Використовуйте команду `!donate`. Ми цінуємо вашу підтримку!\n\n"
                "**🔖 Якими проектами володіє Андрій Мухамед?**\n"
                "**Game Quest**, **Nanson**, **ANIME INDUSTRY**, **KINO INDUSTRY**, **Стримус**.\n\n"
                "**🔖 Як стати частиною команди?**\n"
                "Ми відкриті для талановитих людей! Пишіть нам.\n\n"
                "**🔖 Де знайти ваш контент?**\n"
                "На Telegram, YouTube та інших платформах. Посилання на всі проекти [тут](https://muhamedlabs.pro)\n\n"
                "**📜 Залишилися питання?**\n"
                "Напишіть нам! Ваше задоволення — наша мета."
    }
}

def get_translation(key, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(key, {}).get(lang, translations[key]["ru"])  # Если нет перевода, возвращаем русский