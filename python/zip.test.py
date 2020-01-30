#
# Zip Code Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from zip import is_valid_zip_code

class TestZip(unittest.TestCase):

    def test_valid(self):
        expected = True
        actual = is_valid_zip_code("12345")
        
        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = False
        actual = is_valid_zip_code("54b12")
        
        self.assertEqual(expected, actual)

    def test_short_str(self):
        expected = False
        actual = is_valid_zip_code("1234")

        self.assertEqual(expected, actual)

    def test_long_str(self):
        expected = False
        actual = is_valid_zip_code("123456")

        self.assertEqual(expected, actual)

    def test_negative(self):
        expected = False
        actual = is_valid_zip_code("-1234")

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = False
        actual = is_valid_zip_code("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        is_valid_zip_code("12345")
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
