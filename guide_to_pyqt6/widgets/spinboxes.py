"""
spinboxes.py
by HundredVisionsGuy
A demo of the two main types of spinboxes
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QSpinBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window Title")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)

        layout = QVBoxLayout()

        title_text = "Tip Calculator"
        title_label = QLabel(title_text)

        # TODO: Create HBox that gets a number with a decimal point
        amount_layout = QHBoxLayout()
        amount_label = QLabel("Order Amount: ")
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0, 1000.00)
        self.amount_input.setPrefix("$")
        self.amount_input.setSingleStep(0.5)
        amount_layout.addWidget(amount_label)
        amount_layout.addWidget(self.amount_input)

        # TODO: Create An HBox Layout with a QSpinBox that gets a whole number
        tip_layout = QHBoxLayout()
        tip_label = QLabel("Tip Amount: ")
        self.tip_input = QSpinBox()
        self.tip_input.setSingleStep(5)
        self.tip_input.setSuffix("%")
        tip_layout.addWidget(tip_label)
        tip_layout.addWidget(self.tip_input)

        # TODO: Add 2 buttons in an hbox: one for calculating & a clear button
        button_layout = QHBoxLayout()
        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calculate)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(calc_button)
        button_layout.addWidget(clear_button)

        # TODO: Create an output label to display the instructions and results
        self.instructions = "Enter a dollar amount using decimal number, and a"
        self.instructions += " tip amount as a whole number (ex. 10, 15, 20), "
        self.instructions += "then click calculate or clear to reset."

        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        """
        Challenge: make a simple calculator app that uses 2 inputs.
            * Pick a math or science formula (like area of circle or force).
            * Change the instructions to explain what the user should do.
            * Format the results by rounding the output to 2 decimal places.
            * Format the output using clear language.
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addLayout(amount_layout)
        layout.addLayout(tip_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.instructions_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def calculate(self):
        dollar_amount = self.amount_input.value()
        dollar_amount = round(dollar_amount, 2,)
        tip = self.tip_input.value()
        tip_amount = dollar_amount * (tip * 0.01)
        tip_amount = round(tip_amount, 2)
        total_amount = dollar_amount + tip_amount
        total_amount = round(total_amount, 2)

        output = f"You entered ${dollar_amount:.2f} for the amount, "
        output += f"and {tip}% for your tip.\n"
        output += f"You should therefore tip ${tip_amount:.2f}, and "
        output += f"the total bill should come to ${total_amount:.2f}."
        self.instructions_label.setText(output)

    def clear(self):
        self.amount_input.setValue(0)
        self.tip_input.setValue(0)
        self.instructions_label.setText(self.instructions)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
