from abc import ABC, abstractmethod


class IProduct(ABC):
    pass


class ProductA(IProduct):
    pass


class ProductB(IProduct):
    pass


class ICreator(ABC):

    @abstractmethod
    def create_product(self) -> IProduct:
        pass


class CreatorA(ICreator):

    def create_product(self) -> IProduct:
        return ProductA()


class CreatorB(ICreator):

    def create_product(self) -> IProduct:
        return ProductB()


if __name__ == '__main__':
    creator_a = CreatorA()
    creator_b = CreatorB()

    product_a_one = creator_a.create_product()
    product_b_two = creator_a.create_product()

    product_a_one = creator_b.create_product()
    product_b_two = creator_b.create_product()
