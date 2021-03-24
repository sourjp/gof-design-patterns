"""I referred below sample.

https://ja.wikipedia.org/wiki/Composite_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from __future__ import annotations
from abc import ABC, abstractmethod

from typing import Optional


class Item(ABC):

    def __init__(self, name: str) -> None:
        self.name = name
        self.parent: Optional[Item] = None

    @property
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def print(self, path: str = '') -> None:
        pass


class File(Item):

    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int) -> None:
        self.__size = size

    def print(self, path: str = '') -> None:
        print(f'{path}/{self.name} ({self.size})')


class Directory(Item):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.__directory: list[Item] = []

    @property
    def size(self) -> int:
        file_size: int = 0
        for component in self.__directory:
            file_size += component.size
        return file_size

    def add(self, component: Item) -> None:
        self.__directory.append(component)
        component.parent = self

    def remove(self, component: Item) -> None:
        try:
            self.__directory.remove(component)
        except ValueError:
            pass

    def print(self, path: str = '') -> None:
        print(f'{path}/{self.name} ({self.size})')
        for component in self.__directory:
            component.print(f'{path}/{self.name}')


if __name__ == '__main__':
    file1 = File('tmp1.txt', 1)
    file2 = File('tmp2.txt', 20)
    file3 = File('tmp3.txt', 300)
    file4 = File('tmp4.txt', 4000)

    taro_dir = Directory('taro')
    taro_dir.add(file1)
    taro_dir.add(file2)

    home_dir = Directory('home')
    home_dir.add(taro_dir)
    home_dir.add(file3)

    sys_dir = Directory('sys')
    sys_dir.add(file4)

    root_dir = Directory('root')
    root_dir.add(home_dir)
    root_dir.add(sys_dir)

    root_dir.print()
