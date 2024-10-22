from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleMaximumLength(PwdRuleBase):
    MaxLength: int = 42
    Description = f"Password must not contain more than {MaxLength} characters."

    def check(self, password: str) -> bool:
        return len(password) < RuleMaximumLength.MaxLength
