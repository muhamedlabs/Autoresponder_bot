import os
import importlib.util
from BANNED_FILES.config import ADD_MISSION

def load_proces(client):
    """Загружает все файлы автоответов из 'extras_command'."""

    for filename in os.listdir(ADD_MISSION):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Убираем .py
            module_path = os.path.join(ADD_MISSION, filename)

            spec = importlib.util.spec_from_file_location(module_name, module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Если в модуле есть функция register_proces, вызываем её
            if hasattr(module, "register_proces"):
                module.register_proces(client)