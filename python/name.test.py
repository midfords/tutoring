#
# Name Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from name import is_valid_name

class TestName(unittest.TestCase):

    def test_valid(self):
        expected = True
        actual = is_valid_name("mary modern")
        
        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = False
        actual = is_valid_name("a11an 7ur1ng")
        
        self.assertEqual(expected, actual)

    def test_short_str(self):
        expected = False
        actual = is_valid_name("y ng")

        self.assertEqual(expected, actual)

    def test_multiple_spaces(self):
        expected = False
        actual = is_valid_name("brenda albright grand")

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = False
        actual = is_valid_name("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        is_valid_name("mary modern")
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
