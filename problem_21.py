"""
Amicable numbers
-------------------

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from utils.timer import time_it
from utils.math import proper_divisors

#-------------------------------------------------------------------------------------------------

def d(n):
    """ Returns the sum of all proper divisors of n. """
    return sum(proper_divisors(n))


def are_amicable(n, dn):
    """ Returns True if n and dn are amicable, or False otherwise. """
    if n == dn:
        return False

    return d(dn) == n


@time_it
def problem_21():

    amicables = set()
    for n in range(10000):
        if are_amicable(n, d(n)):
            amicables.add(n)
            amicables.add(d(n))

    print(sum(amicables))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_21()
