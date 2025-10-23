from BANNED_FILES.config import RedisManager
from redis_storage.users_contest import UsersContest

redis = RedisManager()

async def get_user_language(user_id: str) -> str:
    """
    Повертає мову користувача за його ID з Redis.
    Якщо користувач не знайдений — повертає "ru".
    """

    try:
        async with redis:
            record = await redis.load(UsersContest, key=str(user_id))

            if record is None:
                print(f"[DEBUG] Користувач {user_id} не знайдений у Redis. Використовуємо 'ru'.")
                return "ru"

            language = getattr(record, "language", None)
            if not language:
                print(f"[DEBUG] У користувача {user_id} не вказана мова. Використовуємо 'ru'.")
                return "ru"

            return language

    except Exception as e:
        print(f"[ERROR] Не вдалося отримати мову користувача {user_id}: {e}")
        return "ru"
