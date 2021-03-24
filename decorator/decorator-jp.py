"""I referred below sample.

https://ja.wikipedia.org/wiki/Decorator_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class Price(ABC):
    """Component"""

    @property
    @abstractmethod
    def value(self) -> int:
        pass


class PrimePrice(Price):
    """ConcreteComponent"""

    def __init__(self, value: int) -> None:
        self.__value = value

    @property
    def value(self) -> int:
        return self.__value


class MarginPrice(Price):
    """Decorator"""

    def __init__(self, price: Price) -> None:
        self.price = price


class WholesalePrice(MarginPrice):
    """ConcreteDecorator"""

    def __init__(self, price: Price, advantage: int) -> None:
        super().__init__(price)
        self.advantage = advantage

    @property
    def value(self) -> int:
        return self.price.value + self.advantage


class DoublePrice(MarginPrice):
    """ConcreteDecorator"""

    def __init__(self, price: Price) -> None:
        super().__init__(price)

    @property
    def value(self) -> int:
        return self.price.value * 2


if __name__ == '__main__':
    price: Price = WholesalePrice(
        DoublePrice(
            WholesalePrice(
                DoublePrice(
                    PrimePrice(120)
                ), 80)
        ), 200)

    print(price.value)
