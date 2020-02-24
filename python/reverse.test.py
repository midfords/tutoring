#
# Reverse Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#

import time
import unittest

from reverse import reverse

class TestReverse(unittest.TestCase):

    def test_word(self):
        pass

    def test_short_word(self):
        pass

    def test_phrase(self):
        pass

    def test_numbers(self):
        pass

    def test_empty(self):
        pass

    def test_runtime(self):
        test_string = "a" * 1000
        start = time.time()
        reverse(test_string)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
