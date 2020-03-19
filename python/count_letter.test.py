#
# Count A Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from count_a import count

class TestCountA(unittest.TestCase):

    def test_lower(self):
        expected = 6
        actual = count("aaaaaa")
        
        self.assertEqual(expected, actual)

    def test_upper(self):
        expected = 8
        actual = count("AAAAAAAA")
        
        self.assertEqual(expected, actual)

    def test_random(self):
        expected = 5
        actual = count("hfytaAFIDsaAAjfkd")
        
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = 0
        actual = count("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = "a" * 1000000
        start = time.time()
        count(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
