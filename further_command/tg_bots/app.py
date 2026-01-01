import asyncio
import os
import importlib
import sys
from pathlib import Path
from telegram.ext import ApplicationBuilder
from BANNED_FILES.config import telegram_bots

def create_app():
    """Создает приложение бота"""
    return ApplicationBuilder().token(telegram_bots).build()

def load_commands_from_terminal(app):
    """Загружает все команды из папки terminal (находится в той же директории)"""
    current_dir = Path(__file__).parent  # Директория tg_bots
    terminal_dir = current_dir / "terminal"
    
    if not terminal_dir.exists():
        return app
    
    # Получаем все Python файлы в папке terminal
    for filename in os.listdir(terminal_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # Убираем .py
            
            try:
                # Создаем полный путь к файлу
                file_path = terminal_dir / filename
                
                # Динамически импортируем модуль
                spec = importlib.util.spec_from_file_location(
                    module_name,
                    file_path
                )
                module = importlib.util.module_from_spec(spec)
                
                # Добавляем модуль в sys.modules для возможности импорта
                sys.modules[f"terminal_{module_name}"] = module
                
                # Выполняем загрузку
                spec.loader.exec_module(module)
                
                # Проверяем наличие функции command_handler
                if hasattr(module, 'command_handler'):
                    handler = module.command_handler()
                    app.add_handler(handler)
                else:
                    print(f"Файл {filename} не содержит функцию command_handler")
                    
            except Exception as e:
                print(f"Ошибка загрузки {filename}: {e}")
                import traceback
                traceback.print_exc()
    
    return app

async def start_mini_bot():
    """Запуск мини-бота"""
    # Создаем приложение
    app = create_app()
    
    # Загружаем команды из папки terminal
    load_commands_from_terminal(app)
    
    # Инициализируем и запускаем бота
    await app.initialize()
    await app.start()
    
    # Запускаем polling
    await app.updater.start_polling()
    
    print("MiniBot is already operating asynchronously!")
    
    # Возвращаем app для контроля
    return app

# Если файл запускается отдельно
if __name__ == "__main__":
    async def main():
        app = await start_mini_bot()
        try:
            # Бесконечный цикл
            while True:
                await asyncio.sleep(3600)
        except KeyboardInterrupt:
            print("Остановка мини-бота...")
            await app.updater.stop()
            await app.stop()
            await app.shutdown()
    
    asyncio.run(main())
