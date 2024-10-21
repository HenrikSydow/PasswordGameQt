from src.pwd_rules.pwd_rule_base import PwdRuleBase
from src.pwd_rules.pwd_validation_result import PwdValidationResult


class PwdValidator:
    def __init__(self, rules: list[PwdRuleBase]) -> None:
        self._rules: list[PwdRuleBase] = rules

    def validate(self, password: str) -> PwdValidationResult:
        result: PwdValidationResult | None = None

        for rule in self._rules:
            if not rule.check(password):
                result = PwdValidationResult(
                    False,
                    rule.Description
                )
                break

        if not result:
            result = PwdValidationResult(
                True,
                "Wow!!! Congratulations! You have passed the validation. :)"
            )

        return result
