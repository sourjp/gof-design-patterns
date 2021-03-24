"""I referred below sample.

https://en.wikipedia.org/wiki/Bridge_pattern
"""

from abc import ABC, abstractmethod

NOT_IMPLEMENTED = 'You should implement this.'


class DrawingAPI(ABC):
    """Implementor"""

    @abstractmethod
    def draw_circle(self, x: float, y: float, radius: float) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED)


class DrawingAPI1(DrawingAPI):
    """ConcreteImplementor"""

    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f'API1.circle at {x}:{y} - radius: {radius:>5.2f}'


class DrawingAPI2(DrawingAPI):
    """ConcreteImplementor"""

    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f'API2.circle at {x}:{y} - radius: {radius:>5.2f}'


class DrawingAPI3(DrawingAPI):
    """ConcreteImplementor"""

    def draw_circle(self, x: float, y: float, radius: float) -> str:
        return f'API3.circle at {x}:{y} - radius: {radius:>5.2f}'


class Shape(ABC):
    """Abstraction"""

    def __init__(self, drawing_api: DrawingAPI) -> None:
        self.drawing_api = drawing_api

    @abstractmethod
    def draw(self) -> str:
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def resize_by_percentage(self, percent: float) -> None:
        raise NotImplementedError(NOT_IMPLEMENTED)


class CircleShape(Shape):
    """RefindAbstraction"""

    def __init__(
            self,
            x: float,
            y: float,
            radius: float,
            drawing_api: DrawingAPI) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(drawing_api)

    def draw(self) -> str:
        return self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def resize_by_percentage(self, percent: float) -> None:
        self.radius *= 1 + percent / 100


if __name__ == '__main__':
    shapes = [
        CircleShape(1.0, 2.0, 3.0, DrawingAPI1()),
        CircleShape(5.0, 7.0, 11.0, DrawingAPI2()),
        CircleShape(5.0, 4.0, 12.0, DrawingAPI3()),
    ]

    for shape in shapes:
        shape.resize_by_percentage(2.5)
        print(shape.draw())
