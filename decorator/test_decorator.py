import unittest

from decorator import StringDisplay, SideBorder, FullBorder


class TestDecorator(unittest.TestCase):

    def test_decorator(self):
        b1 = StringDisplay("Hello, World.")
        b2 = SideBorder(b1, "#")
        b3 = FullBorder(b2)
        b1_result = b1.show()
        b2_result = b2.show()
        b3_result = b3.show()

        b1_want = "Hello, World."
        b2_want = "#Hello, World.#"
        b3_want = "+---------------+|#Hello, World.#|+---------------+"

        self.assertEqual(b1_result, b1_want)
        self.assertEqual(b2_result, b2_want)
        self.assertEqual(b3_result, b3_want)


if __name__ == "__main__":
    unittest.main()
