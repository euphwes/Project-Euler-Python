"""
Distinct primes factors
Problem 47
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first
of these numbers?
"""

from utils.timer import time_it
from utils.primes import get_primes_under
from itertools import count

#-------------------------------------------------------------------------------------------------

# this limit determined experimentally
primes = list(get_primes_under(10**3))

def has_4_distinct_prime_factors(n):
    """ Returns True if n has exactly 4 distinct prime factors, or False otherwise. """

    factor_count = 0
    for p in primes:
        if n % p == 0:
            # if it already has 4 factors so far, another will disqualify it, so just return False
            if factor_count == 4:
                return False
            factor_count += 1

    # we don't have any more than 4 here, but make sure we don't have less
    return factor_count == 4


@time_it
def problem_47():
    for n in count(2):
        if has_4_distinct_prime_factors(n):
            if all(has_4_distinct_prime_factors(n+x) for x in range(1, 4)):
                print(n)
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_47()
