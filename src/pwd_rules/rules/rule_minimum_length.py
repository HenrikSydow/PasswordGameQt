from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleMinimumLength(PwdRuleBase):
    MinLength: int = 12
    Description = f"The password must contain at least {MinLength} characters."

    def check(self, password: str) -> bool:
        return len(password) >= RuleMinimumLength.MinLength
