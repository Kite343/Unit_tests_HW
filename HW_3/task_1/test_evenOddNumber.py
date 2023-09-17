import unittest
from evenOddNumber import even_odd_number


class TestEvenOddNumber(unittest.TestCase):
    def test_odd_positive(self):
        """Нечетное положительное число"""
        self.assertFalse(even_odd_number(3))

    def test_even_positive(self):
        """Четное положительное число"""
        self.assertTrue(even_odd_number(4))

    def test_zero(self):
        """Ноль"""
        self.assertTrue(even_odd_number(0))

    def test_negative_odd(self):
        """Отрицательное нечетное число"""
        self.assertFalse(even_odd_number(-5))

    def test_negative_even(self):
        """Отрицательное четное число"""
        self.assertTrue(even_odd_number(-6))

if __name__ == '__main__':
    unittest.main(verbosity=2)

# python3 -m pip install coverage
# coverage run -m unittest test_evenOddNumber.py -v
# coverage report

# Name                    Stmts   Miss  Cover
# -------------------------------------------
# evenOddNumber.py            2      0   100%
# test_evenOddNumber.py      15      1    93%
# -------------------------------------------
# TOTAL                      17      1    94%