#
# Total Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from total import total

class TestTotal(unittest.TestCase):

    def test_simple_list(self):
        expected = 21
        actual = total([1,2,3,4,5,6])
        
        self.assertEqual(expected, actual)

    def test_complex_list(self):
        expected = 15.2
        actual = total([-3,2.2,4,5,1,6])
        
        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = 0
        actual = total([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = list(range(1, 9999))
        start = time.time()
        total(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
