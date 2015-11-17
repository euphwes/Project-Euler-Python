"""
Non-abundant sums
-----------------

A perfect number is a number for which the sum of its proper divisors is exactly equal to the
number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called
abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
all integers greater than 28123 can be written as the sum of two abundant numbers. However, this
upper limit cannot be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant
numbers.
"""

from utils.math import proper_divisors
from utils.timer import time_it

from itertools import combinations_with_replacement

#-------------------------------------------------------------------------------------------------

def is_abundant(n):
    """ Returns True if n is an abundant integer. That is, the sum of all the proper divisors of n
    is greater than n itself. """
    return sum(proper_divisors(n)) > n


@time_it
def problem_23():
    """ We can set the upper limit for abundant-checking to 20161, since we know this is the
    largest number which cannot be expressed as the sum of two abundant numbers. """

    abundants = list(filter(is_abundant, range(12,20162)))

    abundant_sums = set()
    for a in abundants:
        for b in abundants:
            if a + b < 20162:
                abundant_sums.add(a + b)
            else:
                break

    possibilities = set(range(1,20162))
    print(sum(possibilities - abundant_sums))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_23()
