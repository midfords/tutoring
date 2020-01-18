#
# Palindrome Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from palindrome import isPalindrome

class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):
        expected = True
        actual = isPalindrome("abbcbba")
        
        self.assertEqual(expected, actual)

    def test_not_palindrome(self):
        expected = False
        actual = isPalindrome("abbc")
        
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = True
        actual = isPalindrome("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_str = "x" * 9999
        start = time.time()
        isPalindrome(test_str)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
