"""
form_layouts.py
by HundredVisionsGuy
A demo of a New User type form using the QFormLayout.
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

        # TODO: make layout a QFormLayout
        layout = QVBoxLayout()

        # TODO: Create a title

        # TODO: Create instructions

        # TODO: make an input to get the user's name

        # TODO: make an input to get the user's email

        # TODO: make an input to get the user's password
        # (make it so you cannot see the text)

        # TODO: make an input to confirm the user's password

        # TODO: make a label that will display confirmation

        # TODO: add all the rows to the form

        """
        Challenges:
            * Finish coding the create_user and clear_form methods
            * Style your app
            * Make a personality quiz (ex: which Hogwarts House are you?)
            * Display a warning if any of the following occurs:
                - email doesn't match common guidelines for emails
                - the passwords are not equal
                - the password does not meet the minimum length requirement
                    (min: 8 characters) - hint: len()
                - the password does not include a number or symbol:
                    + you could loop through a string of numbers and check
                        that there is at least one match.
                        Hint: if i in password
                    + you could do the same with symbols.
                    OR
                    + you could use a regular expression
                        https://www.w3schools.com/python/python_regex.asp
        """

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
