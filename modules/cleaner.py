import os
import shutil
import tempfile

from core.module_base import BaseModule


class Module(BaseModule):

    name = "Очистка системы"
    description = "Удаляет временные файлы"
    icon = "🧹"

    def run(self):

        temp = tempfile.gettempdir()
        deleted = 0

        for file in os.listdir(temp):

            path = os.path.join(temp, file)

            try:

                if os.path.isfile(path):
                    os.remove(path)

                else:
                    shutil.rmtree(path)

                deleted += 1

            except:
                pass

        return f"Удалено {deleted} файлов"