from BANNED_FILES.config import RedisManager
from redis_storage.users_contest import UsersContest

redis = RedisManager()

async def get_user_language(user_id: str) -> str:
    """
    Возвращает язык пользователя по его ID из Redis.
    Если пользователь не найден — возвращает "ru".
    """

    try:
        async with redis:
            record = await redis.load(UsersContest, key=str(user_id))

            if record is None:
                print(f"Пользователь {user_id} не найден в Redis. Используем 'ru'.")
                return "ru"

            language = getattr(record, "language", None)
            if not language:
                print(f"У пользователя {user_id} язык не указан. Используем 'ru'.")
                return "ru"

            print(f"Язык пользователя {user_id}: {language}")
            return language

    except Exception as e:
        print(f"Не удалось получить язык пользователя {user_id}: {e}")
        return "ru"
    