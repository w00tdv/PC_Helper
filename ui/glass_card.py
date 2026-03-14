from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *


class GlassCard(QFrame):

    clicked = Signal()

    def __init__(self, module):

        super().__init__()

        self.module = module

        self.setFixedHeight(120)

        self.setStyleSheet("""
        QFrame{
            background: rgba(255,255,255,0.08);
            border-radius:16px;
            border:1px solid rgba(255,255,255,0.15);
        }
        """)

        self.init_ui()

        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(120)

    def init_ui(self):

        layout = QHBoxLayout()

        if self.module.icon:

            icon = QLabel()
            pix = QPixmap(self.module.icon).scaled(48,48)

            icon.setPixmap(pix)

            layout.addWidget(icon)

        text_layout = QVBoxLayout()

        name = QLabel(self.module.name)
        name.setStyleSheet("font-size:18px;color:white;")

        desc = QLabel(self.module.description)
        desc.setStyleSheet("color:rgba(255,255,255,0.6);")

        text_layout.addWidget(name)
        text_layout.addWidget(desc)

        layout.addLayout(text_layout)

        self.setLayout(layout)

    def mousePressEvent(self, e):

        self.clicked.emit()

    def enterEvent(self, event):

        self.setStyleSheet("""
        QFrame{
            background: rgba(255,255,255,0.15);
            border-radius:16px;
            border:1px solid rgba(255,255,255,0.25);
        }
        """)

    def leaveEvent(self, event):

        self.setStyleSheet("""
        QFrame{
            background: rgba(255,255,255,0.08);
            border-radius:16px;
            border:1px solid rgba(255,255,255,0.15);
        }
        """)