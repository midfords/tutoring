# 
# Primes
#
# Python tutoring exercise.
# Sean Midford, 2020
#

def isPrime(n):
    """This function takes an integer n, and checks if it is a prime number.
    A prime number is defined as a number that is only divisible by 1 and itself.
    Negative numbers are not prime numbers. 0 is not a prime number.

    Parameters
    ----------
    n : int
        The number to be checked.
    
    Returns
    -------
    bool
        True if the number is prime, otherwise False.
    """
    for i in range(2, n):
        if n % i == 0:
            return False;

    return n > 0


if __name__ == "__main__":
    print("Do not run this file directly. \nRun the test file instead: python primes.test.py")