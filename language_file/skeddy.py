import random

translations = {
    "skeddy": {
        "ru": [
               "🎯 **Не забудь о стратегической встрече с командой Game Quest.** Новый проект ждет твоих идей! Это отличная возможность обсудить свежие концепции и определить ключевые этапы разработки. Убедись, что у команды есть все ресурсы для успешного старта. 🚀",
               "🌍 **Время обсудить расширение Nanson.** Новые рынки — это новые возможности! Подготовь аналитику и предложения, чтобы презентовать их на встрече с партнерами. Не забудь про маркетинговую стратегию для захвата новых аудиторий. 📊",
               "🎬 **Твой план для ANIME INDUSTRY требует обновления.** Запланируй мозговой штурм на этой неделе. Собери команду, чтобы обсудить новые анимационные проекты и возможности коллабораций с японскими студиями. 🎨",
               "🍿 **KINO INDUSTRY ждет твоих креативных решений.** Не забудь о встрече с продюсерами! Обсуди новые сценарии, бюджеты и возможности для создания блокбастеров, которые покорят мировые экраны. 🎥",
               "🎮 **Стримус нуждается в новых фишках.** Подумай, как сделать платформу еще круче. Возможно, стоит добавить новые функции для стримеров или улучшить пользовательский интерфейс. Проведи опрос среди пользователей, чтобы узнать их ожидания. 💡",
                "🌐 **Время разработать новую амбициозную цель для всех проектов.** Что дальше — мировое доминирование? Собери ключевых руководителей, чтобы обсудить долгосрочную стратегию и определить приоритеты на ближайшие годы. 🚀",
               "🏆 **Не забудь о наградах и признании.** Подавай заявки на престижные премии в индустрии. Это не только повысит репутацию проектов, но и привлечет внимание новых партнеров и инвесторов. 💼",
               "📈 **Твой план масштабирования требует детализации.** Запланируй рабочую сессию на эту тему. Обсуди с командой, какие ресурсы необходимы для расширения и как оптимизировать текущие процессы. 🔧",
               "🌟 **Время найти новые таланты для команды.** Запланируй собеседования и нетворкинг. Новые люди принесут свежие идеи и энергию, которые помогут проектам расти быстрее. 💪",
               "💰 **Не забудь о финансовом планировании.** Новые цели требуют четкого бюджета. Проведи встречу с финансовым отделом, чтобы обсудить инвестиции, расходы и потенциальные источники дохода. 📊",
               "💻 **Твоя идея о глобальном хакатоне требует подготовки.** Начни планировать уже сейчас! Определи тематику, пригласи экспертов и разработай программу, которая вдохновит участников на создание инновационных решений. 🚀",
               "🎨 **Время обновить брендинг всех проектов.** Новые логотипы, новые идеи! Проведи встречу с дизайнерами и маркетологами, чтобы обсудить, как сделать визуальную идентификацию более современной и запоминающейся. 🖌️",
               "🤝 **Не забудь о встрече с инвесторами.** Новые цели требуют новых ресурсов. Подготовь убедительную презентацию, которая покажет потенциал проектов и убедит инвесторов в их успешности. 💼",
               "📰 **Твой план по созданию собственного медиа-портала требует деталей.** Время действовать! Определи целевую аудиторию, контент-стратегию и технические требования для запуска. 🚀",
               "📚 **Не забудь о собственном развитии.** Новые навыки — новые горизонты для всех проектов! Запланируй обучение или курсы, которые помогут тебе оставаться в курсе последних трендов и технологий. 🌟",
            ],

        "uk": [
               "🎯 **Не забудь про стратегічну зустріч із командою Game Quest.** Новий проект чекає на твої ідеї! Це чудова нагода обговорити свіжі концепції та визначити ключові етапи розробки. Переконайся, що в команди є всі ресурси для успішного старту. 🚀",
               "🌍 **Час обговорити розширення Nanson.** Нові ринки — це нові можливості! Підготуй аналітику та пропозиції, щоб презентувати їх на зустрічі з партнерами. Не забудь про маркетингову стратегію для захоплення нових аудиторій. 📊",
               "🎬 **Твій план для ANIME INDUSTRY потребує оновлення.** Заплануй мозковий штурм на цьому тижні. Збери команду, щоб обговорити нові анімаційні проекти та можливості співпраці з японськими студіями. 🎨",
               "🍿 **KINO INDUSTRY чекає на твої креативні рішення.** Не забудь про зустріч із продюсерами! Обговори нові сценарії, бюджети та можливості для створення блокбастерів, які підкорять світові екрани. 🎥",
               "🎮 **Стримус потребує нових фішок.** Подумай, як зробити платформу ще крутішою. Можливо, варто додати нові функції для стрімерів або покращити користувацький інтерфейс. Проведи опитування серед користувачів, щоб дізнатися про їхні очікування. 💡",
               "🌐 **Час розробити нову амбітну ціль для всіх проектів.** Що далі — світове домінування? Збери ключових керівників, щоб обговорити довгострокову стратегію та визначити пріоритети на найближчі роки. 🚀",
               "🏆 **Не забудь про нагороди та визнання.** Подавай заявки на престижні премії в індустрії. Це не лише підвищить репутацію проектів, але й приверне увагу нових партнерів та інвесторів. 💼",
               "📈 **Твій план масштабування потребує деталізації.** Заплануй робочу сесію на цю тему. Обговори з командою, які ресурси необхідні для розширення та як оптимізувати поточні процеси. 🔧",
               "🌟 **Час знайти нові таланти для команди.** Заплануй співбесіди та нетворкінг. Нові люди принесуть свіжі ідеї та енергію, які допоможуть проектам рости швидше. 💪",
               "💰 **Не забудь про фінансове планування.** Нові цілі потребують чіткого бюджету. Проведи зустріч із фінансовим відділом, щоб обговорити інвестиції, витрати та потенційні джерела доходу. 📊",
               "💻 **Твоя ідея про глобальний хакатон потребує підготовки.** Почни планувати вже зараз! Визнач тематику, запроси експертів та розроби програму, яка надихне учасників на створення інноваційних рішень. 🚀",
               "🎨 **Час оновити брендинг усіх проектів.** Нові логотипи, нові ідеї! Проведи зустріч із дизайнерами та маркетологами, щоб обговорити, як зробити візуальну ідентифікацію сучаснішою та запам’ятовуваною. 🖌️",
               "🤝 **Не забудь про зустріч із інвесторами.** Нові цілі потребують нових ресурсів. Підготуй переконливу презентацію, яка покаже потенціал проектів і переконає інвесторів у їхній успішності. 💼",
               "📰 **Твій план із створення власного медіа-порталу потребує деталей.** Час діяти! Визнач цільову аудиторію, контент-стратегію та технічні вимоги для запуску. 🚀",
               "📚 **Не забудь про власний розвиток.** Нові навички — нові горизонти для всіх проектів! Заплануй навчання чи курси, які допоможуть тобі залишатися в курсі останніх трендів та технологій. 🌟",
            ],

        "en": [
               "🎯 **Don’t forget about the strategic meeting with the Game Quest team.** The new project is waiting for your ideas! This is a great opportunity to discuss fresh concepts and define key development stages. Make sure the team has all the resources for a successful start. 🚀",
               "🌍 **It’s time to discuss the expansion of Nanson.** New markets mean new opportunities! Prepare analytics and proposals to present them at the meeting with partners. Don’t forget about the marketing strategy to capture new audiences. 📊",
               "🎬 **Your plan for ANIME INDUSTRY needs updating.** Schedule a brainstorming session this week. Gather the team to discuss new animation projects and collaboration opportunities with Japanese studios. 🎨",
               "🍿 **KINO INDUSTRY is waiting for your creative solutions.** Don’t forget about the meeting with producers! Discuss new scripts, budgets, and opportunities to create blockbusters that will conquer global screens. �",
               "🎮 **Стримус needs new features.** Think about how to make the platform even cooler. Perhaps it’s worth adding new functions for streamers or improving the user interface. Conduct a survey among users to understand their expectations. 💡",
               "🌐 **It’s time to develop a new ambitious goal for all projects.** What’s next — world domination? Gather key leaders to discuss long-term strategy and set priorities for the coming years. 🚀",
               "🏆 **Don’t forget about awards and recognition.** Apply for prestigious industry awards. This will not only enhance the reputation of the projects but also attract the attention of new partners and investors. 💼",
               "📈 **Your scaling plan needs detailing.** Schedule a working session on this topic. Discuss with the team what resources are needed for expansion and how to optimize current processes. 🔧",
               "🌟 **It’s time to find new talents for the team.** Schedule interviews and networking. New people will bring fresh ideas and energy that will help the projects grow faster. 💪",
               "💰 **Don’t forget about financial planning.** New goals require a clear budget. Meet with the finance department to discuss investments, expenses, and potential revenue sources. 📊",
               "💻 **Your idea for a global hackathon requires preparation.** Start planning now! Define the theme, invite experts, and develop a program that will inspire participants to create innovative solutions. 🚀",
               "🎨 **It’s time to update the branding of all projects.** New logos, new ideas! Meet with designers and marketers to discuss how to make the visual identity more modern and memorable. 🖌️",
               "🤝 **Don’t forget about the meeting with investors.** New goals require new resources. Prepare a compelling presentation that will showcase the potential of the projects and convince investors of their success. 💼",
               "📰 **Your plan to create your own media portal requires details.** It’s time to act! Define the target audience, content strategy, and technical requirements for the launch. 🚀",
               "📚 **Don’t forget about your own development.** New skills — new horizons for all projects! Schedule training or courses that will help you stay up-to-date with the latest trends and technologies. 🌟",
            ],
    }
}

def get_translation(category, lang="ru"):
    """Возвращает перевод по ключу."""
    return translations.get(category, {}).get(lang, translations[category]["ru"])  # Если нет перевода, возвращаем русский