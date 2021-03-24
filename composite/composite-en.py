"""I referred below sample.

https://en.wikipedia.org/wiki/Composite_pattern
"""

from abc import ABC, abstractmethod


class Graphic(ABC):
    """Component"""

    @abstractmethod
    def print(self) -> None:
        pass


class CompositeGraphic(Graphic):
    """Composite"""

    def __init__(self) -> None:
        self.child_graphics: list[Graphic] = []

    def add(self, graphic: Graphic) -> None:
        self.child_graphics.append(graphic)

    def print(self) -> None:
        print(self.__class__.__name__)
        for graphic in self.child_graphics:
            graphic.print()


class Ellipse(Graphic):
    """Leaf"""

    def print(self) -> None:
        print(f"Ellipse {id(self)}")


if __name__ == '__main__':
    ellipse1 = Ellipse()
    ellipse2 = Ellipse()
    ellipse3 = Ellipse()
    ellipse4 = Ellipse()

    graphic2 = CompositeGraphic()
    graphic2.add(ellipse1)
    graphic2.add(ellipse2)
    graphic2.add(ellipse3)

    graphic3 = CompositeGraphic()
    graphic3.add(ellipse4)

    graphic1 = CompositeGraphic()
    graphic1.add(graphic2)
    graphic1.add(graphic3)

    graphic1.print()

    """
    CompositeGraphic
    CompositeGraphic
    Ellipse 140201961627600
    Ellipse 140201961627552
    Ellipse 140201961627504
    CompositeGraphic
    Ellipse 140201961625488
    """
