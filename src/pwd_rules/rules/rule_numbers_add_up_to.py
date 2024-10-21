from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleNumbersAddUpTo(PwdRuleBase):
    Sum: int = 100
    Description = f"Digits must add up to exactly {Sum}."

    def check(self, password: str) -> bool:
        return sum([int(c) for c in password if c.isnumeric()]) == RuleNumbersAddUpTo.Sum

