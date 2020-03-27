#
# Sort Three Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from sort_three import sort

class TestSortThree(unittest.TestCase):

    def test_sort_case_1(self):
        expected = [1, 2, 3]
        actual = sort(1, 2, 3)

        self.assertEqual(expected, actual)

    def test_sort_case_2(self):
        expected = [1, 2, 3]
        actual = sort(1, 3, 2)

        self.assertEqual(expected, actual)

    def test_sort_case_3(self):
        expected = [1, 2, 3]
        actual = sort(2, 1, 3)

        self.assertEqual(expected, actual)

    def test_sort_case_4(self):
        expected = [1, 2, 3]
        actual = sort(2, 3, 1)

        self.assertEqual(expected, actual)

    def test_sort_case_5(self):
        expected = [1, 2, 3]
        actual = sort(3, 1, 2)

        self.assertEqual(expected, actual)

    def test_sort_case_6(self):
        expected = [1, 2, 3]
        actual = sort(3, 2, 1)

        self.assertEqual(expected, actual)

    def test_sort_negative(self):
        expected = [-3, -2, -1]
        actual = sort(-1, -2, -3)

        self.assertEqual(expected, actual)

    def test_sort_decimal(self):
        expected = [0.00123, 0.0123, 0.123]
        actual = sort(0.123, 0.00123, 0.0123)

        self.assertEqual(expected, actual)

    def test_sort_same(self):
        expected = [0, 0, 0]
        actual = sort(0, 0, 0)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        sort(1, 2, 3)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
