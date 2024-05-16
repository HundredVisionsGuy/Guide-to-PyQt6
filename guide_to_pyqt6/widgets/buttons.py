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
        self.resize(320, 340)

        # Create main layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("A Semi-complete Guide to PyQt6!")
        title_label.setFont(QFont("Calibri", 22, 800, True))
        tagline_label = QLabel("Intro: Project Setup!")
        tagline_label.setFont(QFont("Calibri", 18, 400, True))

        # Challenge Label
        challenge = "<b>Challenge</b>: can you program the button to "
        challenge += "get the name from the name label and display it "
        challenge += "on the output label?"
        extra_challenge = "<b>Extra Challenge</b>: can you add a clear "
        extra_challenge += "button that when clicked removes "
        extra_challenge += "the text from the name input and sets the"
        extra_challenge += " output label back to the initial message?"
        challenge_label = QLabel(challenge)
        challenge_label.setWordWrap(True)
        extra_challenge_label = QLabel(extra_challenge)
        extra_challenge_label.setWordWrap(True)

        # Name input widget
        # TODO: make name_input an instance variable
        name_input = QLineEdit()
        name_input.setPlaceholderText("Your Name:")

        # Push Button widget
        # TODO: attach a click signal
        button = QPushButton("Click me!")

        """
        Challenge: Add a clear button that, when clicked will 
            1. clear the text in the name input
            2. reset the output text to its initial value
        """

        # An output label
        # TODO: make output_label an instance variable
        output_label = QLabel("The output for your button would go here.")
        output_label.setFont(QFont("Calibri", 14, 400))

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(tagline_label)
        layout.addWidget(challenge_label)
        layout.addWidget(extra_challenge_label)
        layout.addWidget(name_input)
        layout.addWidget(button)
        layout.addWidget(output_label)

        # Push contents to the top
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    """
    TODO:
        1. create a custom slot named get_name
        2. make sure it's an instance method
        3. grab the text from the input widget
        4. display that text on the output label
    """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
