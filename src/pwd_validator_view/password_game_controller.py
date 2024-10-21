from src.pwd_validator_view.password_game_widget import PasswordGameWidget
from src.qt_util.async_slot import AsyncSlot
from src.pwd_rules.pwd_validation_result import PwdValidationResult
from src.pwd_rules.pwd_validator import PwdValidator
from src.qt_util.qt_color import QtColor


class PasswordGameController:
    def __init__(self, password_widget: PasswordGameWidget, validator: PwdValidator) -> None:
        self._pwd_widget: PasswordGameWidget = password_widget
        self._validator: PwdValidator = validator

        self._pwd_widget.password_changed.connect(AsyncSlot(self._on_password_changed))

    def _on_password_changed(self, password: str) -> None:
        result: PwdValidationResult = self._validator.validate(password)
        self._pwd_widget.instruction_text = result.reason
        text_color: QtColor = QtColor.Green if result.passed else QtColor.Red
        self._pwd_widget.instruction_text_color = text_color
