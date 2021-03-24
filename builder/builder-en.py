"""I referred below sample.

https://en.wikipedia.org/wiki/Builder_pattern
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Bicycle:

    make: str
    model: str
    colour: str
    height: int


class BicycleBuilder(ABC):

    def __init__(self) -> None:
        self.colour: str
        self.height: int

    @abstractmethod
    def get_result(self) -> Bicycle:
        pass


class GTBuilder(BicycleBuilder):

    def get_result(self) -> Bicycle:
        if self.height == 29:
            return Bicycle('GT', 'Avalanche', self.colour, self.height)
        raise ValueError("MTB height expects 29")


class TREKBuilder(BicycleBuilder):

    def get_result(self) -> Bicycle:
        if self.height == 29:
            return Bicycle('TREK', 'Fuel', self.colour, self.height)
        raise ValueError("MTB height expects 29")


class MountainBikeBuildDirector:

    def __init__(self, builder: BicycleBuilder) -> None:
        self.builder = builder

    def construct(self) -> None:
        self.builder.colour = 'Red'
        self.builder.height = 29


if __name__ == '__main__':
    gt_builder = GTBuilder()
    trek_builder = TREKBuilder()

    gt_director = MountainBikeBuildDirector(gt_builder)
    trek_director = MountainBikeBuildDirector(trek_builder)

    gt_director.construct()
    trek_director.construct()

    gt_bike = gt_builder.get_result()
    trek_bike = trek_builder.get_result()

    print(vars(gt_bike))
    print(vars(trek_bike))
