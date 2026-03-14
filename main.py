import sys

from PySide6.QtWidgets import QApplication

from core.module_loader import load_modules
from ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    modules = load_modules()

    window = MainWindow(modules)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()