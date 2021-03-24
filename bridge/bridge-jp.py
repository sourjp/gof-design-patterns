"""I referred below sample.

https://ja.wikipedia.org/wiki/Bridge_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3#:~:text=Bridge%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%88%E3%83%96%E3%83%AA%E3%83%83%E3%82%B8%E3%83%BB%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%89,%E3%81%93%E3%81%A8%E3%82%92%E7%9B%AE%E7%9A%84%E3%81%A8%E3%81%99%E3%82%8B%E3%80%82
"""

from abc import ABC, abstractmethod


class Material(ABC):
    """Implementor"""

    def __init__(self, name: str) -> None:
        self.name = name


class Wood(Material):
    """ConcreteImplementor"""

    def __init__(self, name: str = 'Wood') -> None:
        super().__init__(name)


class Glass(Material):
    """ConcreteImplementor"""

    def __init__(self, name: str = 'Glass') -> None:
        super().__init__(name)


class Dishware(ABC):
    """Abstraction"""

    def __init__(self, material: Material) -> None:
        self.material = material

    @abstractmethod
    def use(self) -> None:
        pass


class Plate(Dishware):
    """RefindAbstraction"""

    def __init__(self, material: Material) -> None:
        super().__init__(material)
        self.name = 'Plate'

    def use(self) -> None:
        print(f'Use {self.material.name} {self.name}')


class Bowl(Dishware):
    """RefindAbstraction"""

    def __init__(self, material: Material) -> None:
        super().__init__(material)
        self.name = 'Bowl'

    def use(self) -> None:
        print(f'Use {self.material.name} {self.name}')


if __name__ == '__main__':

    wood_plate = Plate(Wood())
    glass_plate = Plate(Glass())
    wood_plate.use()
    glass_plate.use()

    wood_bowl = Bowl(Wood())
    glass_bowl = Bowl(Glass())
    wood_bowl.use()
    glass_bowl.use()
