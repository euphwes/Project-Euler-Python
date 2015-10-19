"""
Quadratic primes
-----------------
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n = 0.
"""

from utils.timer import time_it
from utils.primes import is_prime

#-------------------------------------------------------------------------------------------------

def count_primes_of_quadratic(a, b):
    """ Returns the number of consecutive primes produced by the quadratic equation n² + an + b,
    with n starting at 0. """

    n = 0
    count = 0

    while True:
        if is_prime(n*n + a*n + b):
            count += 1
            n += 1

        else:
            break

    return count


@time_it
def problem_27():
    most_primes_so_far = 0
    coefficient_product = None

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            count = count_primes_of_quadratic(a, b)
            if count > most_primes_so_far:
                most_primes_so_far = count
                coefficient_product = a * b

    print(coefficient_product)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_27()
