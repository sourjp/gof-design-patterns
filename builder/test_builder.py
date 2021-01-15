#!/usr/bin/env python3

import unittest

from builder import Director, TextBuilder


class TestBuilder(unittest.TestCase):
    def test_builder(self):
        tb = TextBuilder()
        director = Director(tb)
        director.construct()
        self.assertEqual(
            tb.get_string(),
            "=====\n「Greeting!」\n\n"
            + "*朝から昼にかけて、\n\n・おはよう。\n・こんにちは。\n\n"
            + "*夜に、\n\n・こんばんは。\n・おやすみ。\n・さようなら。\n\n=====\n")


if __name__ == "__main__":
    unittest.main()
