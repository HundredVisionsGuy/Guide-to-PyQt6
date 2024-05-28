from PyQt6.QtCore import QEvent, QSize, Qt
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QColor
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

python_blue = "#306998"
python_light_blue = "#4B8BBE"
python_gray = "#646464"
python_yellow = "#FFD43B"
python_light_yellow = "#FFE873"


class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(1, 1, 10, 1)
        title_bar_layout.setSpacing(3)
        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(
            """
            QLabel { font-family: "Titillium Web", sans-serif;
                font-size: 16pt; margin-left: 48px;
                color: #efefef; padding: 4px;
                font-weight: 600;}
            """
            )

        if title := parent.windowTitle():
            self.title.setText(title)
            self.title.setFont(QFont("Titillim Web"))
        title_bar_layout.addWidget(self.title)

        # Min button
        self.min_button = QToolButton(self)
        min_icon = QIcon()
        min_icon.addFile("resources/min.svg")
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Max button
        self.max_button = QToolButton(self)
        max_icon = QIcon()
        max_icon.addFile("resources/max.svg")
        self.max_button.setIcon(max_icon)
        self.max_button.setIconSize(QSize(24, 24))
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = QIcon()
        close_icon.addFile("resources/close.svg")

        # Close has only a single state.
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Normal button
        self.normal_button = QToolButton(self)
        normal_icon = QIcon()
        normal_icon.addFile("resources/normal.svg")
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)

        # Add buttons
        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(35, 35))
            button.setStyleSheet(
                """QToolButton {
                    border: none;
                    padding: 2px;
                    color: white;
                }
                """
            )
            button.setIconSize(QSize(26, 26))
            title_bar_layout.addWidget(button)

    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A Semi-complete Guide to PyQt6")
        self.resize(700, 280)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        central_widget = QWidget()
        # This container holds the window contents, so we can style it.
        central_widget.setObjectName("Container")
        central_widget.setStyleSheet(
            """#Container {
            background: qlineargradient(x1:0 y1:0, x2:0 y2:1,
            stop:1 #4584B6 stop:0 #4584B6);
            border-radius: 5px; border: 4px solid black;
            padding: 12px;
        }"""
        )
        self.set_fonts()
        self.title_bar = CustomTitleBar(self)

        work_space_layout = QVBoxLayout()
        work_space_layout.setContentsMargins(30, 5, 11, 11)

        # Set Series Title
        main_title = QLabel("A Basic App")
        main_title.setContentsMargins(5, 5, 25, 5)
        main_title.setFont(QFont("Titillium Web", 46, 600))
        main_title_styles = "color: #fff;"
        main_title.setStyleSheet(main_title_styles)

        more_text = "How to get text input from the user "
        more_text += "and display it on the screen."
        more_label = QLabel(more_text)
        more_label.setContentsMargins(5, 5, 25, 15)
        more_label.setFont(QFont("Titillium Web", 24, 400))
        more_label.setStyleSheet("color: #efefff;")
        more_label.setWordWrap(True)

        work_space_layout.addWidget(main_title)
        work_space_layout.addWidget(more_label)
        # work_space_layout.addWidget(video_title)

        centra_widget_layout = QVBoxLayout()
        centra_widget_layout.setContentsMargins(0, 0, 0, 0)
        centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        centra_widget_layout.addWidget(self.title_bar)
        centra_widget_layout.addLayout(work_space_layout)

        central_widget.setLayout(centra_widget_layout)
        self.setCentralWidget(central_widget)

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()

    def window_state_changed(self, state):
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()

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


def add_drop_shadow(label: QLabel, radius: int,
                    color: str, x_off: int, y_off: int) -> None:
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    shadow.setColor(QColor(color))
    shadow.setOffset(x_off, y_off)
    label.setGraphicsEffect(shadow)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
