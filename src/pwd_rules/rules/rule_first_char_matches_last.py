from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleFirstCharMatchesLast(PwdRuleBase):
    Description = f"First and last character in the password must be the same."

    def check(self, password: str) -> bool:
        return len(password) < 2 or password[0] == password[-1]
