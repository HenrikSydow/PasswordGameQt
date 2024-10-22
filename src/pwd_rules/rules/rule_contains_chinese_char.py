from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsChineseChar(PwdRuleBase):
    Char: str = "㐂"
    Description = f"Password must contain this symbol: {Char}"

    def check(self, password: str) -> bool:
        return RuleContainsChineseChar.Char in password
