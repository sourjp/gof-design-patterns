#!/usr/bin/env python3

import unittest

from iterator import Book, BookShelf


class TestIterator(unittest.TestCase):

    def test_iterator(self):
        books = [Book("Programming Language Go"),
                 Book("Web API The Good Parts"),
                 Book("Mastering TCP/IP")]

        bookshelf = BookShelf()
        for book in books:
            bookshelf.append_book(book)

        iterator = bookshelf.iterator()
        for a, b in zip(iterator, books):
            self.assertEqual(a, b)


if __name__ == '__main__':
    unittest.main()
