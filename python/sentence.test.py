#
# Sentence Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from sentence import sentence_formatter

class TestSentenceFormatter(unittest.TestCase):

    def test_lower(self):
        expected = "This is a sentence."
        actual = sentence_formatter("this is a sentence")
        
        self.assertEqual(expected, actual)

    def test_upper(self):
        expected = "This is a sentence."
        actual = sentence_formatter("THIS IS A SENTENCE")
        
        self.assertEqual(expected, actual)

    def test_periods(self):
        expected = "This is a sentence."
        actual = sentence_formatter("This is a sentence....")

        self.assertEqual(expected, actual)

    def test_valid(self):
        expected = "This is a sentence."
        actual = sentence_formatter("This is a sentence.")

        self.assertEqual(expected, actual)

    def test_multiple(self):
        expected = "This is a sentence. This is a sentence."
        actual = sentence_formatter("this is a sentence. this is a sentence")
        
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = "."
        actual = sentence_formatter("")

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = "word " * 1000
        start = time.time()
        sentence_formatter(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
