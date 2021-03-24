"""I referred below sample.

https://en.wikipedia.org/wiki/Flyweight_pattern
"""


class CheeseBrand:

    def __init__(self, brand: str, cost: float) -> None:
        self.brand = brand
        self.cost = cost
        self._immutable = True  # Disables future attributions

    def __setattr__(self, name, value) -> None:
        if getattr(self, "_immutable", False):  # Allow initial attribution
            raise RuntimeError("This object is immutable")
        else:
            super().__setattr__(name, value)


class CheeseShop:

    # Shared container to access the Flyweights
    menu: dict[str, CheeseBrand] = {}

    def __init__(self) -> None:
        # per-instance container with private attributes
        self.orders: dict[str, int] = {}

    def stock_cheese(self, brand: str, cost: float) -> None:
        self.menu[brand] = CheeseBrand(brand, cost)  # Shared Flyweight

    def sell_cheese(self, brand: str, units: int) -> None:
        self.orders.setdefault(brand, 0)
        self.orders[brand] += units  # Instance attribute

    def total_units_sold(self) -> int:
        return sum(self.orders.values())

    def total_income(self) -> float:
        income: float = 0.0
        for brand, units in self.orders.items():
            income += self.menu[brand].cost * units
        return income


if __name__ == '__main__':
    shop1 = CheeseShop()
    shop2 = CheeseShop()

    shop1.stock_cheese("white", 1.25)
    shop1.stock_cheese("blue", 3.75)
    assert shop1.menu == shop2.menu
    # Now every CheeseShop have 'white' and 'blue' on the inventory
    # The SAME 'white' and 'blue' CheeseBrand

    shop1.sell_cheese("blue", 3)  # Both can sell
    shop2.sell_cheese("blue", 8)  # But the units sold are stored per-instance

    assert shop1.total_units_sold() == 3
    assert shop1.total_income() == 3.75 * 3

    assert shop2.total_units_sold() == 8
    assert shop2.total_income() == 3.75 * 8
