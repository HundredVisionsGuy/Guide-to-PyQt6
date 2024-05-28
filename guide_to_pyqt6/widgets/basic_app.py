"""
basic_app.py
by HundredVisionsGuy
A demo of the most basic input/output: labels, text inputs, and buttons.
"""

import sys
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

        self.setWindowTitle("Basic App")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        title_label = QLabel("Basic App")

        # TODO: add a text input for user's name

        # TODO: add a push button to greet user

        # TODO: add a label to greet user

        """
        Challenges: 
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will 
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
