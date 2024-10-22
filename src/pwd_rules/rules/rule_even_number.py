from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleEvenNumber(PwdRuleBase):
    Description = f"The number of characters is dividable by 2. (It is an even number.)"

    def check(self, password: str) -> bool:
        return len(password) % 2 == 0
