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

        # Create main layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Simple VBox Layout!")
        title_label.setFont(QFont("Calibri", 22, 800, True))
        tagline_label = QLabel("Part 1: Getting started!")
        tagline_label.setFont(QFont("Calibri", 18, 400, True))

        # Name input widget
        name_input = QLineEdit()
        name_input.setPlaceholderText("Your Name:")

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(tagline_label)
        layout.addWidget(name_input)

        # Push contents to the top
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
