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
    QHBoxLayout,
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
        title = "Basic App: a simple greeting app."
        title_label = QLabel(title)

        # add a text input for user's name
        name_layout = QHBoxLayout()
        name_label = QLabel("Your Name: ")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Your Name")
        name_layout.addWidget(name_label)
        name_layout.addWidget(self.name_input)

        # favorite song
        song_layout = QHBoxLayout()
        song_label = QLabel("Favorite Song: ")
        self.song_input = QLineEdit()
        self.song_input.setPlaceholderText("Favorite Song")
        song_layout.addWidget(song_label)
        song_layout.addWidget(self.song_input)

        # add a push button to greet user
        button_layout = QHBoxLayout()
        greet_button = QPushButton("Greet User")
        greet_button.clicked.connect(self.greet_user)
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear)
        button_layout.addWidget(greet_button)
        button_layout.addWidget(clear_button)

        # add a label to greet user
        self.instructions = "Enter name and click button to get a greeting."
        self.greeting_label = QLabel(self.instructions)
        self.greeting_label.setWordWrap(True)

        """
        Challenges:
            * Add another text input (last name, home town, etc.)
            * Add a clear button that, when clicked will
                - clear the text in the name input
                - reset the output text to its initial value
        """

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addLayout(name_layout)
        layout.addLayout(song_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.greeting_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

    def greet_user(self):
        name = self.name_input.text()
        greeting = f"Welcome, {name} to my awesome app of awesomeness. "
        song_title = self.song_input.text()
        if song_title:
            greeting += f"You like {song_title}! That's awesome. Me too!"
        self.greeting_label.setText(greeting)

    def clear(self):
        self.name_input.setText("")
        self.greeting_label.setText(self.instructions)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
