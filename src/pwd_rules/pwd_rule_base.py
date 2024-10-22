from abc import abstractmethod, ABC


class PwdRuleBase(ABC):
    Description: str = "No description available."

    @abstractmethod
    def check(self, password: str) -> bool:
        raise NotImplementedError()
