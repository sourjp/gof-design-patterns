from abc import ABC, abstractmethod
from typing import Any, Sequence


class AbstractExpression(ABC):

    @abstractmethod
    def interpret(self):
        pass


class ExpressionA(AbstractExpression):

    def interpret(self):
        pass


class ExpressionB(AbstractExpression):

    def interpret(self):
        pass


class ExpressionNone(AbstractExpression):

    def interpret(self):
        pass


class Context:

    def __init__(self):
        self.a = ExpressionA()
        self.b = ExpressionB()
        self.none = ExpressionNone()

    def evaluate(self, args: Sequence[Any]):
        for arg in args:
            if arg == 'a':
                self.a(arg)
            elif arg == 'b':
                self.b(arg)
            else:
                self.none(arg)
        return
