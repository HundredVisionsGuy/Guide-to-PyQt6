"""
hbox_layout.py
by HundredVisionsGuy
A simple hbox layout with some vbox layouts for visual interest.

NOTES:
* I started you off on a VBoxLayout so we can add a layout across the top
* Hboxes are a good complement to VBoxes
* Vboxes are a good complement to HBoxes
* Too many combinations make for a confusing UI (if that's you
  then I recommend you use a Grid Layout.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QPushButton,
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
        title_label = QLabel("Title Label (Make this bigger, please!)")

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
