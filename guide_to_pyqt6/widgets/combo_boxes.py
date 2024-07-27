"""
combo_boxes.py
by HundredVisionsGuy
An app that leverages the power of the QComboBox
"""

import sys
from PyQt6.QtGui import QFont, QFontDatabase, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Combo Boxes")
        self.setContentsMargins(12, 12, 12, 12)
        self.resize(320, 240)
        self.set_fonts()

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
        title_label = QLabel("Comboboxes Yo!")
        title_label.setFont(QFont("Titillium Web", 20, 700))

        # add icons
        about_icon = QIcon("resources/icons/info.svg")
        ideas_icon = QIcon("resources/icons/lightbulb.svg")
        expand_icon = QIcon("resources/icons/expand_all.svg")
        collapse_icon = QIcon("resources/icons/collapse_all.svg")
        exit_icon = QIcon("resources/icons/close.svg")

        # TODO: add a QCombobox
        self.options_combobox = QComboBox()
        self.options_combobox.addItem(about_icon, "About")
        self.options_combobox.addItem(ideas_icon, "Ideas")
        self.options_combobox.addItem(expand_icon, "Expand all")
        self.options_combobox.addItem(collapse_icon, "Collapse all")
        self.options_combobox.addItem(exit_icon, "Exit")

        # add all the signals (from QComboBox Signals section that is)
        self.options_combobox.currentIndexChanged.connect(self.index_changed)
        self.options_combobox.currentTextChanged.connect(self.text_changed)
        self.options_combobox.activated.connect(self.activated)
        self.options_combobox.highlighted.connect(self.highlighted)

        # Add a pushbutton
        action_button = QPushButton("Click Me!")
        action_button.clicked.connect(self.perform_action)

        # Output label
        self.instructions = "Try selecting different options, then click"
        self.instructions += " the button to see what happens."
        self.output_label = QLabel(self.instructions)

        # add widgets & layouts to main layout
        layout.addWidget(title_label)
        layout.addWidget(self.options_combobox)
        layout.addWidget(action_button)
        layout.addWidget(self.output_label)

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

    def perform_action(self):
        selected = self.options_combobox.currentText()
        output = f"You selected {selected} for your option."
        self.output_label.setText(output)

    def index_changed(self, index):
        if index == 1:
            idea = "Here's an idea: Learn a new hobby or skill."
            self.output_label.setText(idea)
        elif index == 2:
            self.showMaximized()
        elif index == 3:
            self.showNormal()

    def text_changed(self, text):
        print(f"Text was changed, text being {text}.")

    def activated(self, info):
        print(f"Combobox activated: form of {info}. Shape of {info}")

    def highlighted(self, thing):
        print(f"{thing} is being highlighted, yo!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
