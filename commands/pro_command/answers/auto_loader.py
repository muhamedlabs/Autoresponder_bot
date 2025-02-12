import os
import importlib.util

def load_auto_responses(client):
    """Загружает все файлы автоответов из 'commands/pro_command/answers'."""
    folder = "commands/pro_command/answers"

    for filename in os.listdir(folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Убираем .py
            module_path = os.path.join(folder, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Если в модуле есть функция register_auto_reply, вызываем её
            if hasattr(module, "register_auto_reply"):
                module.register_auto_reply(client)

    print("All autoresponses have been uploaded!")
