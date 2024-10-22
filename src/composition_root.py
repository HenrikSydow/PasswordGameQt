import sys
from PySide6.QtWidgets import QApplication

from src.pwd_rules.rules.rule_at_most_n_digits_in_a_row import RuleAtMostNDigitsInARow
from src.pwd_rules.rules.rule_contains_calc_result import RuleContainsCalcResult
from src.pwd_rules.rules.rule_contains_chinese_char import RuleContainsChineseChar
from src.pwd_rules.rules.rule_contains_lambda import RuleContainsLambda
from src.pwd_rules.rules.rule_contains_lowercase_letter import RuleContainsLowercaseLetter
from src.pwd_rules.rules.rule_contains_number import RuleContainsNumber
from src.pwd_rules.rules.rule_contains_special_character import RuleContainsSpecialCharacter
from src.pwd_rules.rules.rule_contains_uppercase_letter import RuleContainsUppercaseLetter
from src.pwd_rules.rules.rule_contains_weird_char_sequence import RuleContainsWeirdCharSequence
from src.pwd_rules.rules.rule_maximum_length import RuleMaximumLength
from src.pwd_rules.rules.rule_numbers_add_up_to import RuleNumbersAddUpTo
from src.pwd_rules.rules.rule_upper_lower_alternating import RuleUpperLowerAlternating
from src.pwd_validator_view.password_game_controller import PasswordGameController
from src.pwd_validator_view.password_game_widget import PasswordGameWidget
from pwd_rules.pwd_validator import PwdValidator
from pwd_rules.rules.rule_minimum_length import RuleMinimumLength
from window import Window


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)

    pwd_game_widget: PasswordGameWidget = PasswordGameWidget()
    validator: PwdValidator = PwdValidator(
        [
            RuleMinimumLength(),
            RuleContainsUppercaseLetter(),
            RuleContainsLowercaseLetter(),
            RuleContainsSpecialCharacter(),
            RuleContainsNumber(),
            RuleNumbersAddUpTo(),
            RuleAtMostNDigitsInARow(),
            RuleContainsLambda(),
            RuleUpperLowerAlternating(),
            RuleContainsCalcResult(),
            RuleMaximumLength(),
            RuleContainsChineseChar(),
            RuleContainsWeirdCharSequence()
        ]
    )

    window: Window = Window("Password Game")
    window.setCentralWidget(pwd_game_widget)

    _: PasswordGameController = PasswordGameController(pwd_game_widget, validator)

    app.exec()
