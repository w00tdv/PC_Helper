from PySide6.QtWidgets import *
from PySide6.QtCore import *

from services.weather_service import get_weather


class HeaderWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setFixedHeight(160)

        self.init_ui()

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()
        self.update_weather()

    def init_ui(self):

        root = QHBoxLayout()

        root.addStretch()

        self.card = QFrame()
        self.card.setObjectName("timeCard")

        layout = QVBoxLayout()

        self.clock = QLabel()
        self.clock.setObjectName("clock")

        self.weather = QLabel("Загрузка погоды...")
        self.weather.setObjectName("weather")

        self.clock.setAlignment(Qt.AlignCenter)
        self.weather.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.clock)
        layout.addWidget(self.weather)

        self.card.setLayout(layout)

        root.addWidget(self.card)

        root.addStretch()

        self.setLayout(root)

    def update_time(self):

        from datetime import datetime

        self.clock.setText(datetime.now().strftime("%H:%M"))

    def update_weather(self):

        w = get_weather()

        if w:
            self.weather.setText(w)