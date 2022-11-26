import unittest

import main


class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.mo.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(main.mo.sub(2, 3), 1)

    def test_mul(self):
        self.assertEqual(main.mo.mul(2, 3), 6)

    def test_div(self):
        self.assertEqual(main.mo.div(2, 6), 3)

