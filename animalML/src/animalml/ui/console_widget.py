from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
QWidget,
QVBoxLayout,
QPlainTextEdit
) 

class ConsoleWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        console_log = QPlainTextEdit()
        console_log.setReadOnly(True)
        console_log.setFont(QFont("Courier"))

        # default start message, should only be displayed on click of start train btn
        console_log.appendPlainText("Training started...")

        # I will add plumbing to actually accept console logs later

        layout.addWidget(console_log)

        self.setLayout(layout)
