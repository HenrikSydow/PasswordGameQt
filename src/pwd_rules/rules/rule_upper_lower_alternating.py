from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleUpperLowerAlternating(PwdRuleBase):
    Description = "Upper- and lowercase characters must be alternating."

    def check(self, password: str) -> bool:
        last_char: str = ""
        for c in password:
            if last_char:
                if (
                    (last_char.isupper() and c.isupper()) or
                    (last_char.islower() and c.islower())
                ):
                    return False
            last_char = c
        return True
