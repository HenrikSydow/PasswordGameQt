from dataclasses import dataclass


@dataclass
class PwdValidationResult:
    passed: bool
    reason: str
