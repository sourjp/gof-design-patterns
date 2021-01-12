#!/usr/bin/env python3

class Book(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class BookShelf(object):
    def __init__(self):
        self.books = []

    def append_book(self, book):
        self.books.append(book)

    def iterator(self):
        """iterator を外に出すことで再利用性を高める"""
        return BookShelfIterator(self.books)


class BookShelfIterator(object):
    """BookShelfIterator としているが、magic methodsを使えば共通実装にもできる"""

    def __init__(self, book_shelf):
        self._book_shelf = book_shelf
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._book_shelf):
            raise StopIteration()
        book = self._book_shelf[self._index]
        self._index += 1
        return book
