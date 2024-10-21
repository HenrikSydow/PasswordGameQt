from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleAtMostNDigitsInARow(PwdRuleBase):
    MaxDigits: int = 3
    Description = f"There can be at most {MaxDigits} consecutive digits. (Separate them using characters.)"

    def check(self, password: str) -> bool:
        consecutive: int = 0
        for c in password:
            if c.isnumeric():
                consecutive += 1
            else:
                consecutive = 0
            if consecutive > RuleAtMostNDigitsInARow.MaxDigits:
                return False
        return True

