#
# Summer Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from phone import isValidPhone

class TestPhone(unittest.TestCase):

    def test_valid(self):
        expected = True
        actual = isValidPhone("4535212542")
        
        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = False
        actual = isValidPhone("431a423153")
        
        self.assertEqual(expected, actual)

    def test_short_string(self):
        expected = False
        actual = isValidPhone("214312")

        self.assertEqual(expected, actual)

    def test_long_string(self):
        expected = False
        actual = isValidPhone("34213453451")

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = False
        actual = isValidPhone("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        isValidPhone("4123532523")
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
