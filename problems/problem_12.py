"""
Highly divisible triangular number
----------------------------------

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle
number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors. What is the value of
the first triangle number to have over five hundred divisors?
"""

from utils.sequences import triangle_numbers
from utils.primes import prime_factors
from utils.timer import time_it

from collections import Counter

from functools import reduce

#-------------------------------------------------------------------------------------------------

def count_factors(n):
    """ Counts the total number of divisors/factors of the provided number.

    Here's the gist from http://mathforum.org/library/drmath/view/55843.html:

    A number n can be represented as:  n = x^a + y^b + z^c + ...
    where x, y, z ... are the prime factors of n, and a, b, c, ... are their multiplicities.

    The number of total divisors of n = (a+1) * (b+1) * (c+1) * ...
    """

    # builds a dict-like Counter object, where the keys are the distinct prime factors, and the
    # values are the multiplicity of that factor (aka, how many of that distinct factor were
    # present in the prime factorization)
    prime_factor_counter = Counter(prime_factors(n))

    # get a list of the multiplicities of the prime factors + 1
    prime_factor_multiplicities_plus_one = [(x + 1) for _, x in prime_factor_counter.most_common()]

    # multiply those all together and return
    multiply = lambda x, y: x * y
    return reduce(multiply, prime_factor_multiplicities_plus_one, 1)


@time_it
def problem_12():
    for num in triangle_numbers():
        if count_factors(num) > 500:
            print(num)
            break

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_12()