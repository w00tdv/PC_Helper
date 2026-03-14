from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox
from datetime import datetime

schedule = {
    "07:30": "Проснуться",
    "07:45": "Завтрак",
    "08:00": "Гейнер",
    "10:30": "Перекус",
    "13:00": "Обед",
    "16:00": "Перекус",
    "17:30": "Конец работы",
    "17:40": "Тренировка",
    "18:10": "Протеин",
    "18:30": "Ужин",
    "21:00": "Перекус",
    "23:00": "Подготовка ко сну",
}


class RoutineAlerts:

    def __init__(self, window):

        self.window = window

        self.timer = QTimer()
        self.timer.timeout.connect(self.check)
        self.timer.start(30000)

    def check(self):

        now = datetime.now().strftime("%H:%M")

        if now in schedule:

            QMessageBox.information(
                self.window,
                "Напоминание",
                schedule[now]
            )