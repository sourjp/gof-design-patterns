"""I referred below sample.

https://ja.wikipedia.org/wiki/Flyweight_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""


class Stamp:

    def __init__(self, type: str) -> None:
        self.type = type

    def __str__(self) -> str:
        return self.type


class StampFactory:
    # To share in instances, use class var.
    # __pool: dict[str, Stamp] = {}

    def __init__(self) -> None:
        self.__pool: dict[str, Stamp] = {}

    def get(self, type: str) -> Stamp:
        # print(f'pool: {self.__pool.keys()}')
        return self.__pool.setdefault(type, Stamp(type))


if __name__ == '__main__':
    stamp_factory = StampFactory()
    stamps = [stamp_factory.get(char) for char in ['A', 'B', 'A', 'C', 'B']]
    for stamp in stamps:
        print(stamp)
