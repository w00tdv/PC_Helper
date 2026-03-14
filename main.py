import sys

from PySide6.QtWidgets import QApplication

from core.module_loader import load_modules
from ui.main_window import MainWindow
from ui.styles import APP_STYLE


def main():

    app = QApplication(sys.argv)

    app.setStyleSheet(APP_STYLE)

    modules = load_modules()

    window = MainWindow(modules)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()