#
# Min Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import random
import unittest

from min import min

class TestMin(unittest.TestCase):

    def test_positive_numbers(self):
        expected = 1
        actual = min([1, 2, 3])
        
        self.assertEqual(expected, actual)

    def test_negative_numbers(self):
        expected = -10
        actual = min([-10, 0, 20])
        
        self.assertEqual(expected, actual)

    def test_duplicate_numbers(self):
        expected = 1
        actual = min([1, 1, 10])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = list(range(1, 999999))
        random.shuffle(test_list)
        start = time.time()
        min(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
