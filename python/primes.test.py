#
# Primes Tests
#
# Python tutoring exercise test cases.
# Sean Midford, 2020
#
import time
import unittest

from primes import isPrime

class TestPrimes(unittest.TestCase):

    def test_prime(self):
        expected = True
        actual = isPrime(5)

        self.assertEqual(expected, actual)

    def test_non_prime(self):
        expected = False
        actual = isPrime(6)

        self.assertEqual(expected, actual)

    def test_zero(self):
        expected = False
        actual = isPrime(0)

        self.assertEqual(expected, actual)

    def test_negative_prime(self):
        expected = False
        actual = isPrime(-5)

        self.assertEqual(expected, actual)

    def test_negative_non_prime(self):
        expected = False
        actual = isPrime(-6)

        self.assertEqual(expected, actual)

    def test_runtime(self):
        start = time.time()
        isPrime(99999999)
        runtime = time.time() - start

        self.assertTrue(runtime < 1.0)


if __name__=='__main__':
    unittest.main()
