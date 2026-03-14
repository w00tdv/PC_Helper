from core.module_base import BaseModule
from PySide6.QtWidgets import *
from datetime import datetime


schedule = {
    "07:30": "🔔 Проснуться",
    "07:45": "🍳 Завтрак",
    "08:00": "🥤 Гейнер",
    "10:30": "🍞 Перекус",
    "13:00": "🍽 Обед",
    "16:00": "🍌 Перекус",
    "17:30": "💻 Конец работы",
    "17:40": "🏋️ Тренировка",
    "18:10": "🥤 Протеин",
    "18:30": "🍽 Ужин",
    "21:00": "🍌 Перекус",
    "23:00": "🌙 Подготовка ко сну",
    "23:30": "😴 Сон",
}


class Module(BaseModule):

    name = "📅 Расписание дня"
    description = "Тренировки, еда и режим"
    icon = "📅"

    def run(self):

        dialog = QDialog()
        dialog.setWindowTitle("Мой режим дня")

        layout = QVBoxLayout()

        now = datetime.now().strftime("%H:%M")

        for time, task in schedule.items():

            label = QLabel(f"{time} — {task}")

            if time == now:
                label.setStyleSheet("font-weight:bold;")

            layout.addWidget(label)

        dialog.setLayout(layout)

        dialog.exec()