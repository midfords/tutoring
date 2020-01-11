#
# Complete Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import random
import unittest

from complete import isComplete

class TestComplete(unittest.TestCase):

    def test_complete_ordered(self):
        expected = True
        actual = isComplete([1,2,3,4,5,6])
        
        self.assertEqual(expected, actual)

    def test_complete_unordered(self):
        expected = True
        actual = isComplete([3,2,4,5,1,6])
        
        self.assertEqual(expected, actual)

    def test_not_complete(self):
        expected = False
        actual = isComplete([1,2,3,5,6])

        self.assertEqual(expected, actual)

    def test_empty(self):
        expected = True
        actual = isComplete([])

        self.assertEqual(expected, actual)

    def test_runtime(self):
        test_list = list(range(1, 999999))
        random.shuffle(test_list)
        start = time.time()
        isComplete(test_list)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
