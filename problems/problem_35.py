"""
Circular primes
---------------

The number, 197, is called a circular prime because all rotations of the digits:197, 971, and 719,
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from utils.timer import time_it
from utils.primes import is_prime

#-------------------------------------------------------------------------------------------------

def rotate(l, n):
    """ Rotates the list l by n items and returns it. """
    return l[n:] + l[:n]


def is_circular_prime(n):
    """ Returns True is n is a circular prime: that is, if n itself is prime, as are all rotations
    of its digits. """

    # if n itself is not prime, it's certainly not a circular prime
    if not is_prime(n):
        return False

    # convert n to a list of digits so we can rotate it
    n = list(str(n))

    # For every rotation of the digits of n, convert that back into an int, and check primality
    # If any of them are not, return False
    rotated_number = lambda list, i: int(''.join(rotate(list, i)))
    if any(not is_prime(rotated_number(n, i)) for i in range(1, len(n))):
        return False

    # We made it here, so n and all rotations of n are prime
    return True


@time_it
def problem_35():
    circular_primes = list(filter(is_circular_prime, range(10**6)))
    print(len(circular_primes))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_35()
