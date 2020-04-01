#
# Mod List Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from mod_list import mod

class TestModList(unittest.TestCase):

    def test_positives(self):
        expected = [1, 0, 1]
        actual = mod([1, 2, 3], 2)

        self.assertEqual(expected, actual)

    def test_negatives(self):
        expected = [1, 0, 1]
        actual = mod([-5, -10, -15], 2)

        self.assertEqual(expected, actual)

    def test_decimals(self):
        expected = [1.5, 0.6, 1.7]
        actual = mod([5.5, 10.6, 15.7], 2)

        self.assertEqual(expected, actual)

    def test_duplicates(self):
        expected = [1, 0, 1, 1, 0]
        actual = mod([1, 2, 3, 3, 2], 2)

        self.assertEqual(expected, actual)

    def test_mod_by_zero(self):
        expected = []
        actual = mod([1, 2, 3, 3, 2], 0)

        self.assertEqual(expected, actual)

    def test_mod_by_one(self):
        expected = [0, 0, 0, 0, 0]
        actual = mod([1, 2, 3, 3, 2], 1)

        self.assertEqual(expected, actual)

    def test_mod_by_negative(self):
        expected = [-1, 0, -1, -1, 0]
        actual = mod([1, 2, 3, 3, 2], -2)

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = []
        actual = mod([], 2)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = [4] * 1000000
        start = time.time()
        mod(test_list, 2)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
