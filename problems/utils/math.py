""" Utility module for general math-y stuff. """

from .primes import prime_factors
from itertools import combinations
from functools import reduce

#-------------------------------------------------------------------------------------------------

def proper_divisors(n):
    """ Returns the list of all proper divisors of n. """

    multiply = lambda x, y: x * y

    # Get the prime factors of n
    factors = prime_factors(n)

    # Build up divisors by getting the product of every possible combination of prime factors
    divisors = [1]
    for i in range(1, len(factors)):
        for combo in combinations(factors, i):
            divisors.append(reduce(multiply, combo, 1))

    # Weed out the duplicate divisors by running the list through a set, and then sort the set
    # to get a sorted list back
    return sorted(set(divisors))
