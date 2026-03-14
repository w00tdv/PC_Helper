from PySide6.QtWidgets import *
from PySide6.QtCore import *

from ui.glass_card import GlassCard


class MainWindow(QMainWindow):

    def __init__(self, modules):

        super().__init__()

        self.modules = modules

        self.resize(900,600)

        self.setWindowTitle("PC Helper")

        self.init_ui()

    def init_ui(self):

        scroll = QScrollArea()

        container = QWidget()
        layout = QVBoxLayout()

        title = QLabel("PC Helper")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:32px;")

        layout.addWidget(title)

        for module in self.modules:

            card = GlassCard(module)

            card.clicked.connect(lambda m=module: self.run_module(m))

            layout.addWidget(card)

        layout.addStretch()

        container.setLayout(layout)

        scroll.setWidget(container)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

    def run_module(self, module):

        result = module.run()

        QMessageBox.information(self, module.name, str(result))