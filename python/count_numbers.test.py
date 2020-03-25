#
# Count Numbers Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from count_numbers import count

class TestCountNumbers(unittest.TestCase):

    def test_numbers(self):
        expected = 6
        actual = count("123456")
        
        self.assertEqual(expected, actual)

    def text_all_numbers(self):
        expected = 10
        actual = count("0123456789")

        self.assertEqual(expected, actual)

    def text_duplicate_numbers(self):
        expected = 6
        actual = count("111111")

        self.assertEqual(expected, actual)

    def test_letters(self):
        expected = 0
        actual = count("AAAAAA")
        
        self.assertEqual(expected, actual)

    def test_random(self):
        expected = 5
        actual = count("hf1yta2AFI4Dsa5AAj3fkd")
        
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = 0
        actual = count("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = "0" * 1000000
        start = time.time()
        count(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
