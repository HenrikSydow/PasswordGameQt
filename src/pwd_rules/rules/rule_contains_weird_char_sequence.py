from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsWeirdCharSequence(PwdRuleBase):
    CharSequence: str = "ݒڞݞ"
    Description = f"Password must contain this sequence: {CharSequence}"

    def check(self, password: str) -> bool:
        return RuleContainsWeirdCharSequence.CharSequence in password
