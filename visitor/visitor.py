"""I referred below sample.

https://en.wikipedia.org/wiki/Visitor_pattern
https://ja.wikipedia.org/wiki/Visitor_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class CarElementVisitor(ABC):

    @abstractmethod
    def visit_body(self, element: Body) -> None:
        raise NotImplementedError

    @abstractmethod
    def visit_engine(self, element: Engine) -> None:
        raise NotImplementedError

    @abstractmethod
    def visit_wheel(self, element: Wheel) -> None:
        raise NotImplementedError

    @abstractmethod
    def visit_car(self, element: Car) -> None:
        raise NotImplementedError


class CarElementPrintVisitor(CarElementVisitor):

    def visit_body(self, body: Body) -> None:
        print("Visiting body.")

    def visit_engine(self, engine: Engine) -> None:
        print("Visiting engine.")

    def visit_wheel(self, wheel: Wheel) -> None:
        print("Visiting {} wheel.".format(wheel.name))

    def visit_car(self, car: Car) -> None:
        print("Visiting car.")


class CarElementDoVisitor(CarElementVisitor):

    def visit_body(self, body: Body) -> None:
        print("Moving my body.")

    def visit_engine(self, engine: Engine) -> None:
        print("Starting my engine.")

    def visit_wheel(self, wheel: Wheel) -> None:
        print("Kicking my {} wheel.".format(wheel.name))

    def visit_car(self, car: Car) -> None:
        print("Starting my car.")


class CarElement(ABC):

    @abstractmethod
    def accept(self, visitor: CarElementVisitor) -> None:
        raise NotImplementedError


class Body(CarElement):

    def accept(self, visitor: CarElementVisitor) -> None:
        visitor.visit_body(self)


class Engine(CarElement):

    def accept(self, visitor: CarElementVisitor) -> None:
        visitor.visit_engine(self)


class Wheel(CarElement):

    def __init__(self, name: str) -> None:
        self.name = name

    def accept(self, visitor: CarElementVisitor) -> None:
        visitor.visit_wheel(self)


class Car(CarElement):

    def __init__(self) -> None:
        self.elements = [
            Wheel('front left'), Wheel('front right'),
            Wheel('back left'), Wheel('back right'),
            Body(), Engine()
        ]

    def accept(self, visitor: CarElementVisitor) -> None:
        for element in self.elements:
            element.accept(visitor)
        visitor.visit_car(self)


if __name__ == '__main__':
    car = Car()
    car.accept(CarElementPrintVisitor())
    # Visiting front left wheel.
    # Visiting front right wheel.
    # Visiting back left wheel.
    # Visiting back right wheel.
    # Visiting body.
    # Visiting engine.
    # Visiting car.

    car.accept(CarElementDoVisitor())
    # Kicking my front left wheel.
    # Kicking my front right wheel.
    # Kicking my back left wheel.
    # Kicking my back right wheel.
    # Moving my body.
    # Starting my engine.
    # Starting my car.
