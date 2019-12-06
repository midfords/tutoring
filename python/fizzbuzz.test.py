# 
# Fizzbuzz Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2019
#
import time
import unittest

from fizzbuzz import fizzbuzz

class TestFizzbuzz(unittest.TestCase):

    def test_fizz(self):
        expected = "fizz"
        actual0 = fizzbuzz(3)
        actual1 = fizzbuzz(9)

        self.assertEqual(expected, actual0)
        self.assertEqual(expected, actual1)

    def test_buzz(self):
        expected = "buzz"
        actual0 = fizzbuzz(5)
        actual1 = fizzbuzz(20)

        self.assertEqual(expected, actual0)
        self.assertEqual(expected, actual1)

    def test_fizzbuzz(self):
        expected = "fizzbuzz"
        actual0 = fizzbuzz(0)
        actual1 = fizzbuzz(15)
        actual2 = fizzbuzz(45)

        self.assertEqual(expected, actual0)
        self.assertEqual(expected, actual1)
        self.assertEqual(expected, actual2)

    def test_empty_string(self):
        expected = ""
        actual = fizzbuzz(1)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        expected = "fizz"
        start = time.time()
        actual = fizzbuzz(99999999)
        runtime = time.time() - start

        self.assertEqual(expected, actual)
        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()