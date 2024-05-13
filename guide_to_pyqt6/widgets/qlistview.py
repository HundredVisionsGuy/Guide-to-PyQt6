"""
qlistview.py
by HundredVisionsGuy
A bare bones starter code to begin with.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QListWidget,
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
        title_label = QLabel("ListView WIdget")

        # TODO: create your list widget

        # TODO: add items to your list widget

        # TODO: add a button to test getting input from the list widget

        """
        Advanced TODO
        1. check out the dos at https://doc.qt.io/qt-6/qlistwidget.html
        2. explore the public methods
        3. check out the slots and signals
        4. customize your QListWidget
        5. style your QListWidget
        """

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
