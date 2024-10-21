from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsUppercaseLetter(PwdRuleBase):
    Description = "Password must contain at least one uppercase letter."

    def check(self, password: str) -> bool:
        return len([c for c in password if c.isupper()]) > 0
