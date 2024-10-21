from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsLowercaseLetter(PwdRuleBase):
    Description = "Password must contain at least one lowercase letter."

    def check(self, password: str) -> bool:
        return len([c for c in password if c.islower()]) > 0
