from PySide6.QtWidgets import *
from PySide6.QtCore import *


class HeaderWidget(QWidget):

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()

        self.clock = QLabel()
        self.clock.setObjectName("clockBox")

        self.clock.setAlignment(Qt.AlignCenter)

        self.clock.setFixedSize(90, 36)

        layout.addWidget(self.clock)

        layout.addStretch()

        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):

        from datetime import datetime

        self.clock.setText(datetime.now().strftime("%H:%M"))