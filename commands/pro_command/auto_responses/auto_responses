import os
import importlib.util

def load_auto_responses():
    """Загружает все файлы автоответов из 'commands/auto_responses'."""
    responses = {}
    folder = "commands/auto_responses"

    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Убираем .py
            module_path = os.path.join(folder, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Добавляем функцию auto_reply из каждого модуля
            if hasattr(module, "auto_reply"):
                responses[module_name] = module.auto_reply

    return responses
