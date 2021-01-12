import unittest

from template import CharDisplay, StringDisplay


class TestTemplate(unittest.TestCase):
    def test_char_display(self):
        cd = CharDisplay("H")
        self.assertEqual(cd.display(), "<<HHHHH>>")

    def test_string_display(self):
        sd = StringDisplay("Hello World!")
        self.assertEqual(sd.display(), "+------------+\n"
                         + "|Hello World!|\n"
                         + "|Hello World!|\n"
                         + "|Hello World!|\n"
                         + "|Hello World!|\n"
                         + "|Hello World!|\n"
                         + "+------------+")


if __name__ == "__main__":
    unittest.main()
