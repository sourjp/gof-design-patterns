"""I referred below sample.

https://ja.wikipedia.org/wiki/Strategy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class BillingStrategy(ABC):

    @abstractmethod
    def calcurate_price(self, price: int) -> int:
        pass


class NormalStrategy(BillingStrategy):

    def calcurate_price(self, price: int) -> int:
        return price


class HappyHourStrategy(BillingStrategy):

    def calcurate_price(self, price: int) -> int:
        return price // 2


class CustomerBill:

    def __init__(self, strategy: BillingStrategy) -> None:
        self.cart: list[int] = []
        self.strategy = strategy

    def order(self, price: int, qt: int) -> None:
        actual_price = self.strategy.calcurate_price(price * qt)
        self.cart.append(actual_price)

    def pay_off(self) -> None:
        print('Total due: ', sum(self.cart))
        self.cart.clear()


if __name__ == '__main__':

    normal_strategy = NormalStrategy()
    happy_hour_strategy = HappyHourStrategy()

    # Start Today
    first_customer = CustomerBill(normal_strategy)
    first_customer.order(100, 1)

    # Start Happy Hour
    first_customer.strategy = happy_hour_strategy
    first_customer.order(100, 2)

    second_customer = CustomerBill(happy_hour_strategy)
    second_customer.order(80, 1)

    first_customer.pay_off()  # Total due:  200 -> 100 + (100 * 2) //2

    # End Happy Hour
    second_customer.strategy = normal_strategy
    second_customer.order(130, 2)
    second_customer.order(250, 1)
    second_customer.pay_off()  # Total due:  550 -> 80 // 2 + 130 * 2 + 250
