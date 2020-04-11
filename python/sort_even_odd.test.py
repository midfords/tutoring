#
# Sort_Even_Odd
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from sort_even_odd import sort_even_odd


class TestSortEvenOdd(unittest.TestCase):

    def test_positives(self):
        expected = ([2, 4, 6, 8], [0], [1, 3, 5, 7])
        actual = sort_even_odd([0, 1, 2, 3, 4, 5, 6, 7, 8])

        self.assertEqual(expected, actual)

    def test_negatives(self):
        expected = ([-10, -12, -8, -2], [], [-5, -15])
        actual = sort_even_odd([-5, -10, -15, -12, -8, -2])

        self.assertEqual(expected, actual)

    def test_duplicates(self):
        expected = ([2], [0, 0], [1, 1, 3, 3])
        actual = sort_even_odd([1, 1, 3, 2, 0, 3, 0])

        self.assertEqual(expected, actual)

    def test_zero(self):
        expected = ([], [0, 0], [])
        actual = sort_even_odd([0, 0])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = ([], [], [])
        actual = sort_even_odd([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = [4, 1, 0] * 100000
        start = time.time()
        sort_even_odd(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__ == '__main__':
    unittest.main()
