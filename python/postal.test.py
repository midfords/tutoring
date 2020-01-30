#
# Postal Code Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from postal import is_valid_postal_code

class TestPostal(unittest.TestCase):

    def test_valid(self):
        expected = True
        actual = is_valid_postal_code("A1B2C3")
        
        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = False
        actual = is_valid_postal_code("A11B2C")
        
        self.assertEqual(expected, actual)

    def test_short_str(self):
        expected = False
        actual = is_valid_postal_code("A1B2")

        self.assertEqual(expected, actual)

    def test_long_str(self):
        expected = False
        actual = is_valid_postal_code("A1B2C3D")

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = False
        actual = is_valid_postal_code("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        is_valid_postal_code("A1B2C3")
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
