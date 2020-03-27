#
# Spell Check Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import os
import time
import unittest

from spell_check import spell_check


class TestSpellCheck(unittest.TestCase):

    def setUp(self):
        path = os.path.dirname(os.path.abspath(__file__))
        words_path = os.path.join(path, 'words.txt')

        with open(words_path, 'rb') as f:
            self.words = set(f.readlines())

    def test_valid(self):
        expected = 0
        actual = spell_check("hello world", self.words)

        self.assertEqual(expected, actual)

    def test_invalid(self):
        expected = 2
        actual = spell_check("hlelo wrold", self.words)

        self.assertEqual(expected, actual)

    def test_random(self):
        expected = 5
        actual = spell_check(
            "this is a lnog sentnence and it hhas many mispellled wrods", self.words)

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = 0
        actual = spell_check("", self.words)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_string = "word " * 1000000
        start = time.time()
        spell_check(test_string, self.words)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__ == '__main__':
    unittest.main()
