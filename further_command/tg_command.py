import sys
import asyncio
from telegram import Bot
from BANNED_FILES.config import TG_CHANNEL_ID, telegram_bots, START_GIF


class ConsoleToTelegram:
    def __init__(self):
        self.original_stdout = sys.__stdout__
        self.original_stderr = sys.__stderr__
        self.bot: Bot | None = None
        self.initialized = False

        # Пропуск первых сообщений
        self._messages_to_skip = 2
        self._skipped = 0

        # Задержка старта
        self._delay_seconds = 10
        self._delay_active = True
        self._buffer: list[str] = []

    async def init_bot(self):
        try:
            self.bot = Bot(token=telegram_bots)
            await self.bot.get_me()
            self.initialized = True

            # GIF старт и сообщения
            try:
                await self.bot.send_animation(
                    chat_id=TG_CHANNEL_ID,
                    animation=START_GIF,
                    caption=(
                            "🌌 **Console Activated!**\n\n"
                            "Логи проснулись и готовы к работе. Также нейроны прогрелись, мозг сети активирован. Ну й пропускаем первые 3 сообщения, чтобы ничего не шумело.\n\n"
                            "Канал готов ловить сигналы из консоли в реальном времени, И пусть данные текут, как электрические искры!"
                            ),

                    parse_mode="Markdown"
                )

            except Exception as e:
                # Не фатально
                self.original_stdout.write(
                    f"[ConsoleLogger] startup GIF warning: {e}\n"
                )

            # Таймер задержки запуска
            asyncio.create_task(self._delayed_flush())

            return True

        except Exception as e:
            self.original_stdout.write(f"[ConsoleLogger] init failed: {e}\n")
            return False

    async def _delayed_flush(self):
        await asyncio.sleep(self._delay_seconds)

        self._delay_active = False

        if not self._buffer:
            return

        for msg in self._buffer:
            await self._send(msg)
            await asyncio.sleep(0.05)

        self._buffer.clear()

    def write(self, text):
        # всегда пишем в обычную консоль
        self.original_stdout.write(text)

        if not self.initialized:
            return

        if not text.strip():
            return

        # Пропуск первых сообщений
        if self._skipped < self._messages_to_skip:
            self._skipped += 1
            return

        # Если задержка активна — буферизуем
        if self._delay_active:
            self._buffer.append(text)
            return

        # После задержки — сразу отправляем
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self._send(text))
        except RuntimeError:
            pass

    def flush(self):
        self.original_stdout.flush()

    async def _send(self, text: str):
        try:
            clean = text.rstrip()
            if not clean:
                return

            if len(clean) > 4000:
                parts = [clean[i:i + 4000] for i in range(0, len(clean), 4000)]
                for part in parts:
                    await self.bot.send_message(
                        chat_id=TG_CHANNEL_ID,
                        text=part
                    )
                    await asyncio.sleep(0.05)
            else:
                await self.bot.send_message(
                    chat_id=TG_CHANNEL_ID,
                    text=clean
                )

        except Exception as e:
            self.original_stdout.write(f"[ConsoleLogger] send failed: {e}\n")


# Один глобальный экземпляр
_console_logger: ConsoleToTelegram | None = None


def get_console_capture() -> ConsoleToTelegram:
    global _console_logger
    if _console_logger is None:
        _console_logger = ConsoleToTelegram()
    return _console_logger


async def setup_console_logger() -> bool:
    logger = get_console_capture()
    return await logger.init_bot()
