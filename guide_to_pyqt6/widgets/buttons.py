"""
buttons.py
by HundredVisionsGuy
The vbox_layout app but with a button you need to program.
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

        self.setWindowTitle("A Semi-complete Guide to PyQt6!")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        # Create main layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("A Semi-complete Guide to PyQt6!")
        title_label.setFont(QFont("Calibri", 22, 800, True))
        tagline_label = QLabel("Intro: Project Setup!")
        tagline_label.setFont(QFont("Calibri", 18, 400, True))

        # Name input widget
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Your Name:")

        # Push Button widget
        button = QPushButton("Click me!")
        button.clicked.connect(self.get_name)

        """
        Challenge: Add a clear button that, when clicked will 
            1. clear the text in the name input
            2. reset the output text to its initial value
        """

        # An output label
        self.output_label = QLabel("The output for your button would go here.")
        self.output_label.setFont(QFont("Calibri", 14, 400))

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(tagline_label)
        layout.addWidget(self.name_input)
        layout.addWidget(button)
        layout.addWidget(self.output_label)

        # Push contents to the top
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def get_name(self):
        name = self.name_input.text()
        output = f"You entered {name}!"
        self.output_label.setText(output)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
