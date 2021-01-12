#!/usr/bin/env python3

import unittest

from singleton import Singleton


class TestSingleton(unittest.TestCase):

    def test_singleton(self):
        s1 = Singleton.get_instance(10)
        s2 = Singleton.get_instance(10)

        self.assertEqual(id(s1), id(s2))
        self.assertEqual(s1, s2)
        s1.input = 20
        self.assertEqual(s1, s2)


if __name__ == '__main__':
    unittest.main()
