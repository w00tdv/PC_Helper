from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ui.glass_card import GlassCard
from ui.header_widget import HeaderWidget
from ui.styles import DARK, LIGHT
from ui.animated_background import AnimatedBackground
from services.routine_alerts import RoutineAlerts


class MainWindow(QMainWindow):

    def __init__(self, modules):

        super().__init__()

        self.modules = modules
        self.dark = True

        self.resize(800, 600)

        self.init_ui()
        self.apply_theme()

        self.alerts = RoutineAlerts(self)

    def init_ui(self):

        root = QVBoxLayout()
        root.setAlignment(Qt.AlignTop)

        # верхний бар
        top_bar = QHBoxLayout()

        self.header = HeaderWidget()

        top_bar.addWidget(self.header)

        top_bar.addStretch()

        self.theme_btn = QPushButton("🌗")
        self.theme_btn.setFixedSize(36, 36)

        self.theme_btn.clicked.connect(self.toggle_theme)

        top_bar.addWidget(self.theme_btn)

        root.addLayout(top_bar)

        root.addSpacing(30)

        # карточки
        cards_container = QVBoxLayout()

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