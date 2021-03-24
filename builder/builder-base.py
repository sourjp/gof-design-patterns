from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def build_step_one(self):
        pass

    @abstractmethod
    def build_step_two(self):
        pass

    @abstractmethod
    def build_step_three(self):
        pass


class BuilderProductA(Builder):

    def __init__(self):
        pass

    def build_step_one(self):
        pass

    def build_step_two(self):
        pass

    def build_step_three(self):
        pass


class BuilderProductB(Builder):

    def __init__(self):
        pass

    def build_step_one(self):
        pass

    def build_step_two(self):
        pass

    def build_step_three(self):
        pass


class Director:

    def __init__(self, builder: Builder):
        self.__builder = builder

    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder):
        self.__builder = builder

    def construct(self) -> None:
        self.builder.build_step_one()
        self.builder.build_step_two()
        self.builder.build_step_three()


if __name__ == '__main__':
    builder_product_a = BuilderProductA()
    builder_product_b = BuilderProductB()

    director_a = Director(builder_product_a)
    director_a.construct()

    director_b = Director(builder_product_b)
    director_b.construct()
