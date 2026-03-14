from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPainter, QLinearGradient, QColor


class AnimatedBackground(QWidget):

    def __init__(self):

        super().__init__()

        self.offset = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(40)

    def animate(self):

        self.offset += 1

        if self.offset > 1000:
            self.offset = 0

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)

        gradient = QLinearGradient(
            0,
            0,
            self.width(),
            self.height()
        )

        gradient.setColorAt(0, QColor(80, 120, 255))
        gradient.setColorAt(0.5, QColor(140, 70, 255))
        gradient.setColorAt(1, QColor(255, 80, 140))

        painter.fillRect(self.rect(), gradient)