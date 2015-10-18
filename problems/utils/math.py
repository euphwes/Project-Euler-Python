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

#-------------------------------------------------------------------------------------------------

def long_divison(n, d, digit_limit=10):
    """ Calculates n/d (numerator/denominator) by long division. Returns a string representation
    of the result, up to `digit_limit` digits. """

    # Performs integer division on n / d to get the whole number part of the solution
    # Calculate the "new numerator" to be used in the next step of the long division, by taking
    # 10 * (the difference between the current numerator and denominator * result of last step)
    i = n // d
    n = 10 * (n - i * d)

    # If n == 0, the solution was a whole number, and we can return that immediately
    if n == 0:
        return str(i)

    # If we still have a numerator, we're going to have a decimal portion
    # Note the whole number portion as i so we can concatenate it with the decimals when we're
    # done with our calculations
    whole = str(i)

    # Holds the decimal portion's digits of the solution. Convert this into a string when returned
    decimals = ''

    while len(decimals) < digit_limit:
        # Continue long division like described above. Perform integer division on current
        # numerator and denominator, get result, and figure out new numerator based on difference
        i = n // d
        n = 10 * (n - i * d)

        # Append the current result to the decimal portion
        decimals += str(i)

        # If numerator is now 0, the division was clean, and we're done
        if n == 0:
            break

    # Format the full solution with whole number portion + decimal portion
    solution = '{}.{}'.format(whole, decimals)

    # If we still have a numerator left, we hit the digit limit. Append '...' to the result so
    # that the caller knows the solution continues
    if n > 0:
        return solution + '...'

    return solution
