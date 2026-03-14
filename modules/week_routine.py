from core.module_base import BaseModule
from PySide6.QtWidgets import *
from services.routine_data import schedule_week


class Module(BaseModule):

    name = "🗓 Расписание недели"
    description = "Весь план тренировок"
    icon = "🗓"

    def run(self):

        dialog = QDialog()
        dialog.setWindowTitle("План на неделю")

        scroll = QScrollArea()

        container = QWidget()
        layout = QVBoxLayout()

        for day, tasks in schedule_week.items():

            title = QLabel(day)
            title.setStyleSheet("font-weight:bold;font-size:16px")

            layout.addWidget(title)

            for time, task in tasks:

                layout.addWidget(QLabel(f"{time} — {task}"))

            layout.addSpacing(10)

        container.setLayout(layout)

        scroll.setWidget(container)
        scroll.setWidgetResizable(True)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll)

        dialog.setLayout(main_layout)

        dialog.resize(400,500)

        dialog.exec()