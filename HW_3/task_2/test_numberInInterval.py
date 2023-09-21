import unittest
from numberInInterval import number_in_interval

class TestNumberInInterval(unittest.TestCase):
    def test_lower_bound(self):
        self.assertFalse(number_in_interval(25))

    def test_smaller_lower_bound(self):
        self.assertFalse(number_in_interval(2))
        self.assertFalse(number_in_interval(-25))
        self.assertFalse(number_in_interval(-100))

    def test_upper_bound(self):
        self.assertFalse(number_in_interval(100))

    def test_above_upper_bound(self):
        self.assertFalse(number_in_interval(200))


    def test_in_interval(self):
        self.assertTrue(number_in_interval(46))


if __name__ == '__main__':
    unittest.main(verbosity=2)


# python3 -m pip install coverage
# coverage run -m unittest test_numberInInterval.py -v
# coverage report

# Name                       Stmts   Miss  Cover
# ----------------------------------------------
# numberInInterval.py            3      0   100%
# test_numberInInterval.py      17      1    94%
# ----------------------------------------------
# TOTAL                         20      1    95%