from abc import ABC


class Implementor(ABC):
    pass


class ConcreteImplementorA(Implementor):
    pass


class ConcreteImplementorB(Implementor):
    pass


class Abstraction(ABC):

    def __init__(self, implementor: Implementor):
        self.implementor = implementor


class RefindAbstractionA(Abstraction):

    def __init__(self, implementor: Implementor):
        super().__init__(implementor)


class RefindAbstractionB(Abstraction):

    def __init__(self, implementor: Implementor):
        super().__init__(implementor)


if __name__ == '__main__':
    cls_a_impl_a = RefindAbstractionA(ConcreteImplementorA())
    cls_a_impl_b = RefindAbstractionA(ConcreteImplementorB())

    cls_b_impl_a = RefindAbstractionA(ConcreteImplementorA())
    cls_b_impl_b = RefindAbstractionA(ConcreteImplementorB())
