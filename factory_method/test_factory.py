#!/usr/bin/env python3

import unittest

from factory import IDCardFactory


class TestFacotryMethod(unittest.TestCase):
    def test_factory_method(self):
        wants = ["A", "B", "C"]
        factory = IDCardFactory()
        products = [
            factory.create(wants[0]),
            factory.create(wants[1]),
            factory.create(wants[2])
        ]

        for i, product in enumerate(products):
            self.assertEqual(product.use(), wants[i])


if __name__ == "__main__":
    unittest.main()
