from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsSpecialCharacter(PwdRuleBase):
    Description = "Password contains at least one special character."

    def check(self, password: str) -> bool:
        return len([c for c in password.upper() if not (65 <= ord(c) <= 90)]) > 0
