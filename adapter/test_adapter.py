#!/usr/bin/env python3

import unittest

from adapter import PrintBanner, PrintBanner2


class TestBanner(unittest.TestCase):
    def setUp(self):
        self.test_msg = "Hello"
        self.wants = ["(" + self.test_msg + ")", "*" + self.test_msg + "*"]

    def test_print_banner(self):
        pb = PrintBanner(self.test_msg)
        self.assertEqual(pb.print_weak(), self.wants[0])
        self.assertEqual(pb.print_strong(), self.wants[1])

    def test_print_banner2(self):
        pb2 = PrintBanner2(self.test_msg)
        self.assertEqual(pb2.print_weak(), self.wants[0])
        self.assertEqual(pb2.print_strong(), self.wants[1])


if __name__ == '__main__':
    unittest.main()
