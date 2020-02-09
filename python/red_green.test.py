#
# Red Green Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from red_green import is_red_green_even

class TestRedGreen(unittest.TestCase):

    def test_valid(self):
        expected = True
        actual = is_red_green_even(["red", "green"])
        
        self.assertEqual(expected, actual)

    def test_valid_other(self):
        expected = True
        actual = is_red_green_even(["red", "green", "blue"])
        
        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = False
        actual = is_red_green_even(["red", "green", "green"])

        self.assertEqual(expected, actual)

    def test_invalid_other(self):
        expected = False
        actual = is_red_green_even(["red", "green", "blue", "green"])

        self.assertEqual(expected, actual)

    def test_other(self):
        expected = True
        actual = is_red_green_even(["blue", "yellow"])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = True
        actual = is_red_green_even([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = ["red"] * 500 + ["blue"] * 1000 + ["green"] * 500
        start = time.time()
        is_red_green_even(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
