#
# Positive Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from positive import isPositive

class TestPositive(unittest.TestCase):

    def test_positive_number(self):
        expected = True
        actual = isPositive(1)
        
        self.assertEqual(expected, actual)

    def test_negative_number(self):
        expected = False
        actual = isPositive(-1)
        
        self.assertEqual(expected, actual)

    def test_zero(self):
        expected = False
        actual = isPositive(0)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        isPositive(9999999)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
