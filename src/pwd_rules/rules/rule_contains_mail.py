from src.pwd_rules.pwd_rule_base import PwdRuleBase
from re import compile as re_compile, Pattern


class RuleContainsMail(PwdRuleBase):
    MailPattern: Pattern = re_compile(r"^[0-9a-zA-Z+-_~!#$%&´./=^'{}|]+@[a-zA-Z0-9]+\.[comCOM]{3}$")
    Delimiter: str = "|"
    Description = f"The password must contain a valid .com e-mail address, enclosed by this character: \"{Delimiter}\""

    def check(self, password: str) -> bool:
        return any([RuleContainsMail.MailPattern.match(x) for x in password.split("|")])
