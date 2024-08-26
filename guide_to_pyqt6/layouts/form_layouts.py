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
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QFormLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Create Your New User Account")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(420, 250)

        # TODO: make layout a QFormLayout
        layout = QFormLayout()

        # TODO: Create a title
        title_label = QLabel("Create a New User account")

        # TODO: Create instructions
        instructions_text = "Please create a username, email, and password"
        instructions_text += " (make sure your password is a minimum of 8 "
        instructions_text += "characters, includes at least 1 number and one "
        instructions_text += "symbol)."
        instructions_label = QLabel(instructions_text)
        instructions_label.setWordWrap(True)
        instructions_label.setMinimumHeight(60)

        # TODO: make an input to get the user's name
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        # TODO: make an input to get the user's email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("user@domain.com")

        # TODO: make an input to get the user's password
        # (make it so you cannot see the text)
        self.password_input = QLineEdit(echoMode=QLineEdit.EchoMode.Password)

        # TODO: make an input to confirm the user's password
        self.confirm_password_input = QLineEdit(
            echoMode=QLineEdit.EchoMode.Password)

        # TODO: create 2 buttons one to process and one to clear
        self.create_user_button = QPushButton("Create user")
        self.create_user_button.clicked.connect(self.create_user)
        self.clear_button = QPushButton("Clear Form")
        self.clear_button.clicked.connect(self.clear_form)

        # create a horizontal layout for the buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.create_user_button)
        button_layout.addWidget(self.clear_button)

        # TODO: make a label that will display confirmation
        self.confirmation_label = QLabel("")
        self.confirmation_label.setMinimumHeight(40)
        self.confirmation_label.setWordWrap(True)

        # TODO: add all the rows to the form
        layout.addRow(title_label)
        layout.addRow(instructions_label)
        layout.addRow("Username: ", self.username_input)
        layout.addRow("Email: ", self.email_input)
        layout.addRow("Password: ", self.password_input)
        layout.addRow("Confirm Password: ", self.confirm_password_input)
        layout.addRow(button_layout)
        layout.addRow(self.confirmation_label)

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

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def create_user(self):
        # get user info
        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        # check for validity

        # display results
        results = f"Username: {username}, Email: {email}\n"
        results += "Password: -------"
        self.confirmation_label.setText(results)

    def clear_form(self):
        # reset all inputs to emtpy strings
        self.username_input.setText("")
        self.email_input.setText("")
        self.confirmation_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
