"""
vbox_layout.py
by HundredVisionsGuy
A simple VBox Layout - with some standard widgets
"""
import sys
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple VBox Layout")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()

        # create our widgets
        title_label = QLabel("Simple VBox Layout!")

        # TODO: add a text input

        # TODO: add a push button

        # TODO: add another label

        # TODO: add widgets & layouts to main layout
        layout.addWidget(title_label)

        # TODO: move your content up

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
