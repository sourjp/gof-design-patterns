"""I referred below sample.

https://en.wikipedia.org/wiki/Iterator_pattern
https://ja.wikipedia.org/wiki/Iterator_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from collections.abc import Sequence
from typing import Any


class Iterator:

    def __init__(self, data: Sequence[Any], start: int = 0) -> None:
        self.data = data
        self.index = start
        self.end = len(self.data)

    def has_next(self) -> bool:
        return self.index < self.end

    def next(self) -> Any:
        out = self.data[self.index]
        self.index += 1
        return out


class Family:

    def __init__(self) -> None:
        self.family = ["Arthur", "Molly", "Bill", "Charlie",
                       "Percy", "Fred", "George", "Ron", "Ginny"]

    def iterator(self) -> Iterator:
        return Iterator(self.family)


if __name__ == '__main__':
    family = Family()
    family_iterator = family.iterator()

    while family_iterator.has_next():
        print(family_iterator.next())
        # Arthur
        # Molly
        # Bill
        # Charlie
        # Percy
        # Fred
        # George
        # Ron
        # Ginny
