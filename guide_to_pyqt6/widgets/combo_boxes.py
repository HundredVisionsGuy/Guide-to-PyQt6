"""
combo_boxes.py
by HundredVisionsGuy
An app that leverages the power of the QComboBox
"""

import sys
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
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

        """
        TODO List:
            1. set the fonts (see method below)
            2. change the title font and make it bigger using QFont
            3. add a combobox with at least 4 options
            4. try to add an item to the combobox
            5. try to insert an item to the combobox in the middle
            6. add Icons from Google Fonts Icons
            7. add a unique icon to each combobox item
            8. add a push button and make it so clicking the button will
                display the text of the currently selected combobox item.
            9. add signals to the combobox methods
        """

        layout = QVBoxLayout()
        title_label = QLabel("Title Label (Make this bigger, please!)")
        # TODO: make the title bigger and use the Titillium font (or pick one)

        # TODO: add a QCombobox

        # add widgets & layouts to main layout
        layout.addWidget(title_label)

        # [OPTIONAL] Add a stretch to move everything up
        layout.addStretch()

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(widget)

        """
        Bonus Challenge:
            * Read the docs on the qcombobox to expand your learning
                (https://www.pythonguis.com/docs/qcombobox/)
            * Program your app to do something unique based on the
                selection of the combobox (it's your choice on whether
                to have the action for the push button or a signal
                on the combobox)
            * Explore the icons to get ideas on other actions for your
                app.
            * Style your app using the skills from the app_with_style
                challenge
        """

    def set_fonts(self):
        # import fonts
        font_dir = "resources/fonts/"
        heading_font_name = "TitilliumWeb-Black.ttf"
        heading_font_path = font_dir + heading_font_name

        regular_font_name = "TitilliumWeb-Regular.ttf"
        regular_font_path = font_dir + regular_font_name

        # Try and add fonts
        success = QFontDatabase.addApplicationFont(heading_font_path)
        if success == -1:
            print(f"{heading_font_name} not loaded")
        success = QFontDatabase.addApplicationFont(regular_font_path)
        if success == -1:
            print("Regular font not loaded.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
