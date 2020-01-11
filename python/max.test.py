#
# Max Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from max import max

class TestMax(unittest.TestCase):

    def test_positive_numbers(self):
        expected = 3
        actual = max(1, 2, 3)
        
        self.assertEqual(expected, actual)

    def test_negative_numbers(self):
        expected = 20
        actual = max(-10, 0, 20)
        
        self.assertEqual(expected, actual)

    def test_duplicate_numbers(self):
        expected = 10
        actual = max(1, 10, 10)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        max(9999999, -9999999, 0)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
