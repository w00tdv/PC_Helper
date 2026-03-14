import os
import importlib

MODULE_FOLDER = "modules"


def load_modules():
    modules = []

    for file in os.listdir(MODULE_FOLDER):

        if file.endswith(".py") and not file.startswith("_"):
            module_name = file[:-3]

            module = importlib.import_module(f"{MODULE_FOLDER}.{module_name}")

            if hasattr(module, "Module"):
                modules.append(module.Module())

    return modules