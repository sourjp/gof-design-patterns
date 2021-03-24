from abc import ABC
from copy import deepcopy


class IPrototype(ABC):

    def _clone(self):
        return deepcopy(self)


class Product(IPrototype):

    def __init__(self, x: str):
        self.x = x


class NoProdcutException(Exception):
    """There is no searched object in registered object"""


class ProductManager:
    """ProductManager manage specified Product to clone"""

    def __init__(self):
        self.__products = {}

    def register(self, name: str, product: Product):
        # Use deepcopy to avoid reference first object by registered object.
        self.__products[name] = product._clone()

    def create_clone(self, name) -> Product:
        obj = self.__products.get(name)
        if obj is None:
            raise NoProdcutException
        return obj._clone()


if __name__ == '__main__':
    product_x = Product('x')

    manager = ProductManager()
    manager.register('x', product_x)
    copied_x = manager.create_clone('x')
    copied_x.x = 'y'
    assert id(product_x) != id(copied_x)
    assert product_x.x != copied_x.x
