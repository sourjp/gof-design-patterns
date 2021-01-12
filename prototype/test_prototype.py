#!/usr/bin/env python3

import unittest

from prototype import Manager, MessageBox, UnderlinePen


class TestProtoType(unittest.TestCase):
    def test_prototype(self):
        manager = Manager()
        upen = UnderlinePen("~")
        mbox = MessageBox("*")
        sbox = MessageBox("/")
        manager.register("u", upen)
        manager.register("m", mbox)
        manager.register("s", sbox)

        msg = "hello world"
        u1 = manager.create("u")
        self.assertEqual(u1.use(msg), '"hello world"\n ~~~~~~~~~~~ ')
        # self.assertNotEqual(id(upen), id(u1))

        m1 = manager.create("m")
        self.assertEqual(
            m1.use(msg),
            "***************\n* hello world *\n***************")
        # self.assertNotEqual(id(mbox), id(m1))

        s1 = manager.create("s")
        self.assertEqual(
            s1.use(msg),
            "///////////////\n/ hello world /\n///////////////")
        # self.assertNotEqual(id(sbox), id(s1))
        self.assertNotEqual(id(m1), id(s1))


if __name__ == '__main__':
    unittest.main()
