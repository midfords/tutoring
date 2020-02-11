#
# Title Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from title import title_formatter

class TestTitleFormatter(unittest.TestCase):

    def test_lower(self):
        expected = "This Is A Title"
        actual = title_formatter("this is a title")
        
        self.assertEqual(expected, actual)

    def test_upper(self):
        expected = "This Is A Title"
        actual = title_formatter("THIS IS A TITLE")
        
        self.assertEqual(expected, actual)

    def test_spaces(self):
        expected = "This Is A Title"
        actual = title_formatter(" This Is  A   Title   ")
        
        self.assertEqual(expected, actual)

    def test_valid(self):
        expected = "This Is A Title"
        actual = title_formatter("This Is A Title")

        self.assertEqual(expected, actual)

    def test_single(self):
        expected = "Title"
        actual = title_formatter("title")

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = ""
        actual = title_formatter("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = "word " * 1000
        start = time.time()
        title_formatter(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
