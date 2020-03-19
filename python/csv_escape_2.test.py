#
# Csv Escape 2 Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from csv_escape import csv_escape_2

class TestCsvEscape2(unittest.TestCase):

    def test_words(self):
        expected = "one,two,three"
        actual = csv_escape(["one", "two", "three"])
        
        self.assertEqual(expected, actual)

    def test_spaces(self):
        expected = "one two,three four"
        actual = csv_escape(["one two", "three four"])
        
        self.assertEqual(expected, actual)

    def test_commas(self):
        expected = "\"one,two\",\"three,four\""
        actual = csv_escape(["one,two", "three,four"])

        self.assertEqual(expected, actual)

    def test_quotes(self):
        expected = "\"\"\"one\"\",two\",\"three,\"\"four\"\"\""
        actual = csv_escape(["\"one\",two", "three,\"four\""])

        self.assertEqual(expected, actual)

    def test_empty_values(self):
        expected = ","
        actual = csv_escape(["", ""])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = ""
        actual = csv_escape([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = ["\"one\",two"] * 1000000
        start = time.time()
        csv_escape(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
