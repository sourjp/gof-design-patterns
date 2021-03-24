from abc import ABC


class Component(ABC):
    pass


class ConcreteComponent(Component):
    pass


class Decorator(Component):

    def __init__(self, component: Component) -> None:
        self._component = component


class ConcreteDecorator(Decorator):

    def __init__(self, component: Component) -> None:
        super().__init__(component)
