"""I referred below sample.

https://ja.wikipedia.org/wiki/Interpreter_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class Expression(ABC):

    @abstractmethod
    def interpret(self, stack: list[int]) -> None:
        pass


class NumberExpression(Expression):

    def __init__(self, number: int) -> None:
        self.number = number

    def interpret(self, stack: list[int]) -> None:
        stack.append(self.number)


class PlusExpression(Expression):

    def interpret(self, stack: list[int]) -> None:
        right = stack.pop()
        left = stack.pop()
        plus_number = left + right
        stack.append(plus_number)


class MinusExpression(Expression):

    def interpret(self, stack: list[int]) -> None:
        right = stack.pop()
        left = stack.pop()
        minus_number = left - right
        stack.append(minus_number)


class Parser:

    def __init__(self, question: str) -> None:
        self.expression_tree: list[Expression] = []
        self._setup_expression_tree(question)

    def _setup_expression_tree(self, question: str) -> None:
        for token in question.split(' '):
            if token == '+':
                self.expression_tree.append(PlusExpression())
            elif token == '-':
                self.expression_tree.append(MinusExpression())
            else:
                self.expression_tree.append(NumberExpression(int(token)))

    def evaluate(self) -> int:
        context: list[int] = []
        for expression in self.expression_tree:
            expression.interpret(context)
        return context.pop()


if __name__ == '__main__':
    question = "42 4 2 - +"
    parser = Parser(question)
    print(parser.evaluate())  # 44
