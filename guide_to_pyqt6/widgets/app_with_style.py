"""
app_with_style.py
by HundredVisionsGuy
A styling challenge to adjust sizes and styles of
fonts and colors.
"""

import sys
from PyQt6.QtGui import QFont, QFontDatabase
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
        self.resize(320, 240)

        layout = QVBoxLayout()

        # TODO: write a method that will set one or two fonts
        self.set_fonts()

        # TODO: make your title text nice and large and modify the color
        title_text = "Tip Calculator"
        title_label = QLabel(title_text)
        title_label.setFont(QFont("Bebas Neue", 20, 800))
        title_label.setObjectName("title")

        # Order Amount
        amount_layout = QHBoxLayout()
        amount_label = QLabel("Order Amount: ")
        self.amount_input = QDoubleSpinBox()
        self.amount_input.setRange(0, 1000.00)
        self.amount_input.setPrefix("$")
        self.amount_input.setSingleStep(0.5)
        amount_layout.addWidget(amount_label)
        amount_layout.addWidget(self.amount_input)

        # Tip Amount
        tip_layout = QHBoxLayout()
        tip_label = QLabel("Tip Amount: ")
        self.tip_input = QSpinBox()
        self.tip_input.setSingleStep(5)
        self.tip_input.setSuffix("%")
        tip_layout.addWidget(tip_label)
        tip_layout.addWidget(self.tip_input)

        # 2 buttons: one for calculating & a clear button
        button_layout = QHBoxLayout()
        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.calculate)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(calc_button)
        button_layout.addWidget(clear_button)

        # Instructions/Results Label
        self.instructions = "Enter a dollar amount using decimal number, and a"
        self.instructions += " tip amount as a whole number (ex. 10, 15, 20), "
        self.instructions += "then click calculate or clear to reset."

        self.instructions_label = QLabel(self.instructions)
        self.instructions_label.setWordWrap(True)

        """
        Challenge: style this app or your own spinboxes app with the following.
            * Select a color palette for your app.
            * Make sure your app colors have high contrast between light and
              dark.
            * Find a font-pair that goes well with your app but is also
              readable.
            * Try adding a drop-shadow to your title (see the title_screen.py)
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

        # TODO: give the widget a name and set a stylesheet
        widget.setObjectName("MainContainer")

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

    def set_fonts(self):
        # import fonts
        font_dir = "resources/fonts/"
        title_font_name = "BebasNeue-Regular.ttf"
        title_font_path = font_dir + title_font_name

        # Try to add fonts
        success = QFontDatabase.addApplicationFont(title_font_path)
        if success == -1:
            print(f"{title_font_name} not loaded.")

        # You can add another font if you like.


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load stylesheet
    styles_path = "resources/styles.qss"
    stylesheet = None
    with open(styles_path, "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()

    app.exec()
