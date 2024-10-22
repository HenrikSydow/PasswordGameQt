from src.pwd_rules.pwd_rule_base import PwdRuleBase


class RuleContainsCalcResult(PwdRuleBase):
    Formula = "((2.5 * 10 + (-5)) / 4) / 5 + 47"
    Result = eval(Formula)
    Description = f"Password must contain the result of this formula:\n{Formula}"

    def check(self, password: str) -> bool:
        return RuleContainsCalcResult.Result in password