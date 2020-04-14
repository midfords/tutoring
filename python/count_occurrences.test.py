#
# Count Occurrences Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from count_occurrences import count_occurrences

class TestCountOccurrences(unittest.TestCase):

    def test_count(self):
        expected = 2
        actual = count_occurrences([1, "Hi", 3.1415, False, 1], 1)

        self.assertEqual(expected, actual)

    def test_count_no_match(self):
        expected = 0
        actual = count_occurrences([1, "Hi", 3.1415, None, False, 1], 2)

        self.assertEqual(expected, actual)

    def test_count_empty(self):
        expected = 0
        actual = count_occurrences([], 1)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = [1, "Hi", 3.1415, False] * 100000
        start = time.time()
        count_occurrences(test_list, 1)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
