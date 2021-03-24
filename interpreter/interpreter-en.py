"""I referred below sample.

https://en.wikipedia.org/wiki/Interpreter_pattern
"""


class Expr:

    @staticmethod
    def plus(left: int, right: int) -> int:
        return left + right

    @staticmethod
    def minus(left: int, right: int) -> int:
        return left - right

    @staticmethod
    def none(value: int) -> int:
        return value


class ExpressionException(Exception):
    pass


class Parser:

    def parse(self, expression: str) -> int:
        context: list[int] = []
        for token in expression.split(' '):
            self._parse_token(token, context)
        return context.pop()

    def _parse_token(self, token: str, context: list[int]) -> None:
        try:
            result: int
            if token == '+':
                right = context.pop()
                left = context.pop()
                result = Expr.plus(left, right)
            elif token == '-':
                right = context.pop()
                left = context.pop()
                result = Expr.minus(left, right)
            else:
                result = Expr.none(int(token))
            context.append(result)
        except IndexError:
            raise ExpressionException('Expression is incorrect.')


if __name__ == '__main__':
    question = "42 4 2 - +"
    parse = Parser()
    print(parse.parse(question))  # 44
