from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QLineEdit, QVBoxLayout

from src.qt_util.colored_label import ColoredLabel
from src.qt_util.qt_color import QtColor


class PasswordGameWidget(QWidget):
    password_changed: Signal = Signal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._instruction_label: ColoredLabel = ColoredLabel("Please enter your password below:")
        self._instruction_label.setWordWrap(True)
        font: QFont = self._instruction_label.font()
        font.setPointSize(24)
        self._instruction_label.setFont(font)

        self._password_input_field: QLineEdit = QLineEdit()
        self._password_input_field.setPlaceholderText("password")
        self._password_input_field.textChanged.connect(self._on_password_changed)
        self._password_input_field.setFont(font)

        layout: QVBoxLayout = QVBoxLayout()
        layout.addWidget(self._instruction_label)
        layout.addWidget(self._password_input_field)
        self.setLayout(layout)

    @property
    def instruction_text(self) -> str:
        return self._instruction_label.text()

    @instruction_text.setter
    def instruction_text(self, instruction: str) -> None:
        self._instruction_label.setText(instruction)

    @property
    def instruction_text_color(self) -> QtColor:
        return self._instruction_label.fontColor()

    @instruction_text_color.setter
    def instruction_text_color(self, color: QtColor) -> None:
        self._instruction_label.setFontColor(color)

    def _on_password_changed(self, password: str) -> None:
        self.password_changed.emit(password)
