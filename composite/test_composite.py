import unittest

from composite import Directory, File


class TestComposite(unittest.TestCase):

    def test_composite(self):
        got = ""
        try:
            print("Making root...")
            rootdir = Directory("root")
            bindir = Directory("bin")
            tmpdir = Directory("tmp")
            usrdir = Directory("usr")

            rootdir.add(bindir)
            rootdir.add(tmpdir)
            rootdir.add(usrdir)

            bindir.add(File("vi", 10000))
            bindir.add(File("latex", 20000))
            got = rootdir.print_list()
        except FileTreatmentException as e:
            print(e.message)

        self.assertEqual(got, "/root (30000)\n"
                         + "/root/bin (30000)\n"
                         + "/root/bin/vi (10000)\n"
                         + "/root/bin/latex (20000)\n"
                         + "/root/tmp (0)\n"
                         + "/root/usr (0)\n")


if __name__ == "__main__":
    unittest.main()
