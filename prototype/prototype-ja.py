"""I referred below sample.

https://ja.wikipedia.org/wiki/Prototype_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from __future__ import annotations
from abc import ABC
import copy


class Prototype(ABC):

    def __init__(self, value: int) -> None:
        self.value = value

    def clone(self) -> Prototype:
        return copy.deepcopy(self)


class PrototypeFactory(Prototype):

    def __init__(self, value: int) -> None:
        super().__init__(value)


if __name__ == '__main__':
    prototype = PrototypeFactory(1000)
    for i in range(10):
        cloned_prototype = prototype.clone()
        print(f'cls_id: {id(cloned_prototype)}, '
              f'value: {cloned_prototype.value * i}')
