"""I referred below sample.

https://ja.wikipedia.org/wiki/Factory_Method_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod
from typing import Optional, Callable


class Comperator(ABC):
    """Productに相当"""

    @abstractmethod
    def create(self) -> Optional[Callable]:
        pass


class DictionaryOrderComperator(Comperator):
    """ConcreteProductに相当"""

    def create(self) -> Optional[Callable]:
        # デフォルト辞書順なのでNoneで返す
        return None


class LengthOrderComperator(Comperator):
    """ConcreteProductに相当"""

    def create(self) -> Optional[Callable]:
        return lambda letter: len(letter)


class ListPrinter(ABC):
    """Creatorに相当"""

    def print_list(self, words: list[str]) -> None:
        comperator: Comperator = self.create_comperator()
        sort_key: Optional[Callable] = comperator.create()
        if sort_key is None:
            words.sort()
        else:
            words.sort(key=sort_key)
        for word in words:
            print(word)

    @abstractmethod
    def create_comperator(self) -> Comperator:
        pass


class DictionaryOrderListPrinter(ListPrinter):
    """Concreate Creatorに相当"""

    def create_comperator(self) -> Comperator:
        return DictionaryOrderComperator()


class LengthOrderListPrinter(ListPrinter):
    """Concreate Creatorに相当"""

    def create_comperator(self) -> Comperator:
        return LengthOrderComperator()


if __name__ == '__main__':
    words: list[str] = ['いちご', 'もも', 'いちじく']
    print('*' * 50)
    print("・五十音順で表示(デフォルト)")
    dict_printer = DictionaryOrderListPrinter()
    dict_printer.print_list(words=words)

    print('*' * 50)
    print("・長さ順で表示")
    length_printer = LengthOrderListPrinter()
    length_printer.print_list(words=words)
