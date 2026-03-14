from core.module_base import BaseModule
from PySide6.QtWidgets import *
from datetime import datetime
from services.routine_data import schedule_week


class Module(BaseModule):

    name = "📅 Сегодня"
    description = "План на текущий день"
    icon = "📅"

    def run(self):

        days = [
        "Понедельник","Вторник","Среда",
        "Четверг","Пятница","Суббота","Воскресенье"
        ]

        today = days[datetime.today().weekday()]

        dialog = QDialog()
        dialog.setWindowTitle(f"Сегодня — {today}")

        layout = QVBoxLayout()

        for time, task in schedule_week[today]:

            label = QLabel(f"{time} — {task}")

            layout.addWidget(label)

        dialog.setLayout(layout)

        dialog.exec()