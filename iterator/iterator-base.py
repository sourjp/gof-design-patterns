
from abc import ABC, abstractmethod
from typing import Any, Sequence


class Iterator(ABC):

    @abstractmethod
    def next(self) -> bool:
        pass

    @abstractmethod
    def has_next(self):
        pass


class ConcreteIterator(Iterator):

    def __init__(self, data: Sequence[Any], start: int = 0) -> None:
        self.data = data
        self.index = start
        self.end = len(self.data)

    def next(self) -> bool:
        return self.index < self.end

    def has_next(self) -> Any:
        out = self.data[self.index]
        self.index += 1
        return out


class Aggregate(ABC):

    @abstractmethod
    def iterator(self) -> Iterator:
        pass


class ConcreteAggregate(Aggregate):

    def __init__(self):
        self.data: Sequence[Any] = []

    def iterator(self) -> Iterator:
        return ConcreteIterator(self.data)


if __name__ == '__data__':
    ag = ConcreteAggregate()
    ag_iter = ag.iterator()
    while ag_iter.has_next():
        print(ag_iter.next())
