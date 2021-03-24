from abc import ABC, abstractmethod


class IProduct(ABC):
    pass


class IProductA(IProduct):
    pass


class ProductA(IProductA):
    pass


class IProductB(IProduct):
    pass


class ProductB(IProductB):
    pass


class IProductC(ProductB):
    pass


class ProductC(IProductC):
    pass


class Factory(ABC):

    @abstractmethod
    def create_product_a(self) -> IProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> IProductB:
        pass

    @abstractmethod
    def create_product_c(self) -> IProductC:
        pass


class ProductFactory(Factory):

    def create_product_a(self) -> IProductA:
        pass

    def create_product_b(self) -> IProductB:
        pass

    def create_product_c(self) -> IProductC:
        pass
