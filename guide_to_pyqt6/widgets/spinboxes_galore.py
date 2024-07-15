"""
spinboxes_galore.py
by HundredVisionsGuy
A demo of the two main types of spinboxes
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()
        self.instructions = "Make an app that gets two different numbers: "
        self.instructions += "a whole number (integer) and a number with "
        self.instructions += "a decimal point (float). Put them each in "
        self.instructions += "a horizontal layout, and add two buttons: "
        self.instructions += "one that gets then displays the inputs, and "
        self.instructions += "one that resets the inputs and displays these "
        self.instructions += "instructions\n\n"
        self.instructions += "Feel free to modify these instructions once "
        self.instructions += "you are done. Make sure the isntructions are "
        self.instructions += "clear to the user as to what they should do."

        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        # TODO: Create An HBox Layout with a QSpinBox that gets a whole number

        # TODO: Create another HBox that gets a number with a decimal point

        # TODO: Add 2 buttons in an hbox: one for calculating & a clear button

        # TODO: Create an output label to display the instructions and results

        # TODO: Re-write the instructions to tell the user what to do.

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(self.instructions_label)

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
