"""
Largest prime factor
--------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import ceil, sqrt
from utils.timer import timeit

#-------------------------------------------------------------------------------------------------

def is_prime(n):
    """ Returns whether a given number is prime. """

    if n % 2 == 0:
        return False

    for x in range(3, int(sqrt(n)), 2):
        if n % x == 0:
            return False

    return True


def prime_factors(n):
    """ Returns a list of the prime factors of a given number. """

    factors = list()

    while True:
        curr_factor = 2

        if is_prime(n):
            factors.append(n)
            break

        while not is_prime(curr_factor) or not n % curr_factor == 0:
            curr_factor += 1

        factors.append(curr_factor)
        n = int(n / curr_factor)

    return factors


@timeit
def problem_3():
    print(max(prime_factors(600851475143)))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print()
    problem_3()
