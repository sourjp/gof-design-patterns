from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def algorithm(self):
        pass


class StrategyA(Strategy):

    def algorithm(self):
        pass


class StrategyB(Strategy):

    def algorithm(self):
        pass


class Context:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def operation(self):
        self.strategy.algorithm()


if __name__ == '__main__':
    context_a = Context(StrategyA())
    context_b = Context(StrategyB())
