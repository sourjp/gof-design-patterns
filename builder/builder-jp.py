"""I referred below sample.

https://ja.wikipedia.org/wiki/Builder_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3#:~:text=Builder%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%88%E3%83%93%E3%83%AB%E3%83%80%E3%83%BC%E3%83%BB%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%89,%E7%94%9F%E6%88%90%E3%82%92%E5%8F%AF%E8%83%BD%E3%81%AB%E3%81%99%E3%82%8B%E3%80%82
"""

from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from enum import Enum


class Material(Enum):
    WOOD = 0
    CLAY = 1
    CONCRETE = 2
    SNOW = 3


@dataclass(init=False)
class Building:
    base: str
    frame: str
    wall: str


class Builder(ABC):
    @abstractmethod
    def build_base(self) -> None:
        pass

    @abstractmethod
    def build_frame(self) -> None:
        pass

    @abstractmethod
    def build_wall(self) -> None:
        pass

    @abstractproperty
    def building(self) -> Building:
        pass


class JapaneseHouseBuilder(Builder):

    def __init__(self) -> None:
        self.__building = Building()

    def build_base(self) -> None:
        self.__building.base = Material.CONCRETE.name

    def build_frame(self) -> None:
        self.__building.frame = Material.WOOD.name

    def build_wall(self) -> None:
        self.__building.wall = Material.CLAY.name

    @property
    def building(self) -> Building:
        return self.__building


class KamakuraBuilder(Builder):

    def __init__(self) -> None:
        self.__building = Building()

    def build_base(self) -> None:
        self.__building.base = Material.SNOW.name

    def build_frame(self) -> None:
        self.__building.frame = Material.SNOW.name

    def build_wall(self) -> None:
        self.__building.wall = Material.SNOW.name

    @property
    def building(self) -> Building:
        return self.__building


class Director:

    def __init__(self, builder: Builder) -> None:
        self.__builder = builder

    def construct(self) -> Building:
        self.__builder.build_base()
        self.__builder.build_frame()
        self.__builder.build_wall()
        return self.__builder.building


if __name__ == '__main__':
    japanese_house_director = Director(JapaneseHouseBuilder())
    kamakura_director = Director(KamakuraBuilder())

    japanese_house_building = japanese_house_director.construct()
    kamakura_building = kamakura_director.construct()

    # Building(base='CONCRETE', frame='WOOD', wall='CLAY')
    print(japanese_house_building)
    # Building(base='SNOW', frame='SNOW', wall='SNOW')
    print(kamakura_building)
