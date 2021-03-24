"""Use __iter__ and __next__ as pythonic."""

from collections.abc import Sequence, Iterator
from dataclasses import dataclass
from typing import Any


@dataclass
class Book:
    name: str = 'Unknown'
    author: str = 'Unknown'


class BookShelf:

    def __init__(self, books=None) -> None:
        self.books: list[Book]
        if books is None:
            self.books = []
        else:
            self.books = books

    # To write "for book in bookshelf:", implements below.
    #
    # def __iter__(self):
    #     return Iterator(self.books)

    def iterator(self, reverse: bool = False) -> Iterator:
        return MyIterator(self.books, reverse)


class MyIterator(Iterator):

    def __init__(self, data: Sequence[Any], reverse: bool = False) -> None:
        self.data = data
        self.reverse = reverse
        self.index = -1 if self.reverse else 0

    # Unneeded below if inheriting Iterator.
    #
    # def __iter__(self) -> Iterable:
    #     return self

    def __next__(self) -> Iterator:
        try:
            item = self.data[self.index]
            self.index += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration
        return item


if __name__ == '__main__':
    bookshelf = BookShelf([Book('a', 'AAA'), Book('b', 'BBB'), Book()])

    for book in bookshelf.iterator():
        print(book)
        # Book(name='a', author='AAA')
        # Book(name='b', author='BBB')
        # Book(name='Unknown', author='Unknown')

    for book in bookshelf.iterator(reverse=True):
        print(book)
        # Book(name='Unknown', author='Unknown')
        # Book(name='b', author='BBB')
        # Book(name='a', author='AAA')
