"""I referred below sample.

https://ja.wikipedia.org/wiki/Adapter_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3#:~:text=Adapter%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%88%E3%82%A2%E3%83%80%E3%83%97%E3%82%BF%E3%83%BC%E3%83%BB%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%89,%E5%A4%89%E6%9B%B4%E3%81%99%E3%82%8B%E3%81%93%E3%81%A8%E3%81%8C%E3%81%A7%E3%81%8D%E3%82%8B%E3%80%82
"""

from abc import ABC, abstractmethod


class ProductPrice(ABC):
    """Target"""

    @abstractmethod
    def get_doll(self) -> float:
        pass


class Product:
    """Adaptee"""

    def __init__(self, cost: int) -> None:
        self.__cost = cost

    def get_yen(self) -> int:
        return self.__cost


class ProductAdapter(ProductPrice):
    """Adapter"""

    DOLL_RATE: int = 110

    def __init__(self, product: Product) -> None:
        self.__product = product

    def get_doll(self) -> float:
        doll = self.__product.get_yen() / self.DOLL_RATE
        return doll


if __name__ == '__main__':
    product = Product(cost=1000)
    print(f'product cost {product.get_yen()} yen')

    adapted_product = ProductAdapter(product)
    print(f'product cost {adapted_product.get_doll():.1f} doll')
