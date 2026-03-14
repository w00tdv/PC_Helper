from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ui.glass_card import GlassCard
from ui.header_widget import HeaderWidget
from ui.styles import DARK, LIGHT
from ui.animated_background import AnimatedBackground


class MainWindow(QMainWindow):

    def __init__(self, modules):

        super().__init__()

        self.modules = modules
        self.dark = True

        self.resize(800, 600)

        self.init_ui()
        self.apply_theme()

    def init_ui(self):

        root = QVBoxLayout()
        root.setAlignment(Qt.AlignTop)

        header = HeaderWidget()
        root.addWidget(header)

        root.addSpacing(20)

        # контейнер для карточек
        cards_container = QVBoxLayout()
        cards_container.setAlignment(Qt.AlignTop)

        for module in self.modules:

            card = GlassCard(module)

            card.setMaximumWidth(500)

            card.clicked.connect(lambda m=module: self.run_module(m))

            wrapper = QHBoxLayout()
            wrapper.addStretch()
            wrapper.addWidget(card)
            wrapper.addStretch()

            cards_container.addLayout(wrapper)

        root.addLayout(cards_container)

        root.addStretch()

        theme_btn = QPushButton("Сменить тему")
        theme_btn.clicked.connect(self.toggle_theme)

        root.addWidget(theme_btn)

        bg = AnimatedBackground()

        bg.setLayout(root)

        self.setCentralWidget(bg)

    def run_module(self, module):

        result = module.run()

        QMessageBox.information(self, module.name, str(result))

    def toggle_theme(self):

        self.dark = not self.dark
        self.apply_theme()

    def apply_theme(self):

        if self.dark:
            self.setStyleSheet(DARK)
        else:
            self.setStyleSheet(LIGHT)