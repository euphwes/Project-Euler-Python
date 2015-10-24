"""
Goldbach's other conjecture
---------------------------

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of
a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that can't be written as the sum of a prime and twice a square?
"""

from utils.timer import time_it
from utils.primes import get_primes_under, is_prime

#-------------------------------------------------------------------------------------------------

def can_be_written_as_prime_plus_twice_square(n):
    """ Returns True if n can be written as the sum of a prime and twice a square number, or
    returns False otherwise. """

    if is_prime(n):
        return True

    # For every prime under n, find what value of x satisfies:   n = prime + 2x^2
    # If any of those values x are an integer, then n can be written as prime + 2x square number
    for prime in get_primes_under(n):
        x = ((n - prime) / 2) ** 0.5
        if x % 1 == 0:
            return True

    # If we get here, n cannot be written as prime + 2x square number
    return False


@time_it
def problem_46():
    n = 35
    while can_be_written_as_prime_plus_twice_square(n):
        n += 2
    print(n)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_46()
