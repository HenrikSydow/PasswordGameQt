from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsNumber(PwdRuleBase):
    Description = "Password must contain at least one number."

    def check(self, password: str) -> bool:
        return len([c for c in password if c.isnumeric()]) > 0

