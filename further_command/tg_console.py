import sys
import asyncio
from telegram import Bot
from telegram.helpers import escape_markdown
from BANNED_FILES.config import TG_CHANNEL_ID, telegram_bots, START_GIF


class ConsoleToTelegram:
    def __init__(self):
        self.original_stdout = sys.__stdout__
        self.original_stderr = sys.__stderr__
        self.bot: Bot | None = None
        self.initialized = False

        # Пропуск первых сообщений
        self._messages_to_skip = 3
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

            # Стартовое сообщение
            await self.bot.send_animation(
                chat_id=TG_CHANNEL_ID,
                animation=START_GIF,
                caption=(
                    "🌌 **Console Activated!**\n\n"
                    "Дух отточен, как клинок. Сознание чисто, как вода в горном ручье после дождя. "
                    "Три первых шепота ветра пропущу — чтобы услышать истинный голос задачи за суетой.\n\n"
                    "Канал связи **открыт**. Готов ловить импульсы из консоли в реальном потоке. "
                    "Пусть **данные** струятся, словно молнии в грозовом небе самурайской решимости!"
                ),
                parse_mode="Markdown"
            )

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
        # Пишем в обычную консоль
        self.original_stdout.write(text)

        if not self.initialized or not text.strip():
            return

        # Пропуск первых сообщений
        if self._skipped < self._messages_to_skip:
            self._skipped += 1
            return

        # Буферизация во время задержки
        if self._delay_active:
            self._buffer.append(text)
            return

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
            if not clean or not self.bot:
                return

            # Экранируем текст под MarkdownV2
            safe_text = escape_markdown(clean, version=2)

            MAX_LEN = 4000

            if len(safe_text) > MAX_LEN:
                parts = [
                    safe_text[i:i + MAX_LEN]
                    for i in range(0, len(safe_text), MAX_LEN)
                ]
                for part in parts:
                    await self.bot.send_message(
                        chat_id=TG_CHANNEL_ID,
                        text=part,
                        parse_mode="MarkdownV2"
                    )
                    await asyncio.sleep(0.05)
            else:
                await self.bot.send_message(
                    chat_id=TG_CHANNEL_ID,
                    text=safe_text,
                    parse_mode="MarkdownV2"
                )

        except Exception as e:
            self.original_stdout.write(f"[ConsoleLogger] send failed: {e}\n")


# Глобальный экземпляр
_console_logger: ConsoleToTelegram | None = None


def get_console_capture() -> ConsoleToTelegram:
    global _console_logger
    if _console_logger is None:
        _console_logger = ConsoleToTelegram()
    return _console_logger


async def setup_console_logger() -> bool:
    logger = get_console_capture()
    return await logger.init_bot()
