#
# Seconds Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from seconds import seconds

class TestSeconds(unittest.TestCase):

    def test_positive_numbers(self):
        pass

    def test_negative_numbers(self):
        pass

    def test_large_numbers(self):
        pass

    def test_zero(self):
        pass

    def test_runtime(self):
        start = time.time()
        seconds(1, 29, 33, 44)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
