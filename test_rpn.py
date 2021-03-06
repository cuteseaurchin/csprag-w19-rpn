import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)

    def test_minus(self):
        result = rpn.calculate("2 1 -")
        self.assertEqual(1, result)

    def test_carat(self):
        result = rpn.calculate("3 2 ^")
        self.assertEqual(9, result)
