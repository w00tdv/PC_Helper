from PySide6.QtWidgets import *
from PySide6.QtCore import *


class GlassCard(QFrame):

    clicked = Signal()

    def __init__(self, module):

        super().__init__()

        self.module = module

        self.setObjectName("card")

        self.setMinimumHeight(90)
        self.setMaximumHeight(90)

        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )

        self.init_ui()

    def init_ui(self):

        layout = QHBoxLayout()

        layout.setContentsMargins(15, 10, 15, 10)

        icon = QLabel(self.module.icon)
        icon.setObjectName("icon")

        name = QLabel(self.module.name)
        name.setObjectName("title")

        desc = QLabel(self.module.description)
        desc.setObjectName("description")

        text_layout = QVBoxLayout()
        text_layout.addWidget(name)
        text_layout.addWidget(desc)

        layout.addWidget(icon)
        layout.addLayout(text_layout)

        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.clicked.emit()