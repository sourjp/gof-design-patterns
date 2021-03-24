from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self):
        pass


class Composite(Component):

    def __init__(self):
        self.components: list[Component] = []

    def add(self, component: Component):
        self.components.append(component)

    def operation(self):
        pass


class Leaf(Component):

    def operation(self):
        pass


if __name__ == '__main__':
    component1 = Leaf()
    component2 = Leaf()
    component3 = Leaf()
    component4 = Leaf()

    # composite2.components = [component1, component2, component3]
    composite2 = Composite()
    composite2.add(component1)
    composite2.add(component2)
    composite2.add(component3)

    # composite3.components = [component4]
    composite3 = Composite()
    composite3.add(component4)

    # composite1.components = [composite1, composite2]
    composite1 = Composite()
    composite1.add(composite2)
    composite1.add(composite3)

    composite1.operation()
