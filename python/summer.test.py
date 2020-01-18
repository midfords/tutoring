#
# Summer Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from summer import isSummer

class TestSummer(unittest.TestCase):

    def test_early_date(self):
        expected = False
        actual = isSummer(2, 10)
        
        self.assertEqual(expected, actual)

    def test_late_date(self):
        expected = False
        actual = isSummer(11, 1)
        
        self.assertEqual(expected, actual)

    def test_summer_date(self):
        expected = True
        actual = isSummer(8, 21)

        self.assertEqual(expected, actual)

    def test_close_summer_date(self):
        expected = True
        actual = isSummer(6, 21)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        isSummer(7, 30)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
