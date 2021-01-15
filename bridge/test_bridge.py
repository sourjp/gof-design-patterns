import unittest

from bridge import Display, CountDisplay, StringDisplayImpl, CharDisplayImpl


class TestBridge(unittest.TestCase):

    def test_display(self):
        d1 = Display(StringDisplayImpl("Hello, Japan."))
        self.assertEqual(
            d1.display(),
            "+-------------+|Hello, Japan.|+-------------+")

    def test_multidisplay(self):
        d1 = CountDisplay(StringDisplayImpl("Hello, Japan."))
        self.assertEqual(
            d1.multi_display(2),
            "+-------------+|Hello, Japan.||Hello, Japan.|+-------------+")

    def test_char_display(self):
        d1 = Display(CharDisplayImpl("<", "*", ">"))
        self.assertEqual(d1.display(), "<>")
        self.assertEqual(d1.display(), "<*>")
        self.assertEqual(d1.display(), "<**>")


if __name__ == "__main__":
    unittest.main()
