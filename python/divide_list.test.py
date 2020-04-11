#
# Divide List Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from divide_list import divide

class TestDivideList(unittest.TestCase):

    def test_positives(self):
        expected = [0.5, 1, 1.5]
        actual = divide([1, 2, 3])

        self.assertEqual(expected, actual)

    def test_negatives(self):
        expected = [-2.5, -5, -7.5]
        actual = divide([-5, -10, -15])

        self.assertEqual(expected, actual)

    def test_duplicates(self):
        expected = [0.5, 1, 1.5, 1.5, 1]
        actual = divide([1, 2, 3, 3, 2])

        self.assertEqual(expected, actual)

    def test_decimal(self):
        expected = [0.05, 0.25, 0.75]
        actual = divide([0.1, 0.5, 1.5])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = []
        actual = divide([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = [4] * 100000
        start = time.time()
        divide(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
