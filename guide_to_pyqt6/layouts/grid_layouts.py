"""
grid_layouts.py
by HundredVisionsGuy
A demo of the value of grid layouts - for complex layouts

Can you recreate the following grid?

          Column 0      Column 1     Column 2     Column 3 
        +------------+------------+-------------------------+
 Row 0  |              Title screen of the app              |
        +------------+------------+------------+------------+
        |   label    |   label    |   label    |   label    |
 Row 1  |  spinbox   |  spinbox   |  spinbox   |  spinbox   |
        +------------+------------+------------+------------+
        |                         |                         |
 Row 2  |    calculate button     |       clear button      |
        |                         |                         |
        +------------+--------------------------------------+
 Row 3  |                  Output goes here                 |
        +---------------------------------------------------+
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
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
