from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsLambda(PwdRuleBase):
    Lambda: str = "lambda"
    Description = f"Password must contain the phrase \"{Lambda}\"."

    def check(self, password: str) -> bool:
        return RuleContainsLambda.Lambda.lower() in password.lower()
