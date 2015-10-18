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

def long_divison(n, d, digit_limit=10, detect_repetition=False):
    """ Calculates n/d (numerator/denominator) by long division. Returns a string representation
    of the result, up to `digit_limit` digits. if `detect_repetition` is set to True, any digit
    limit is ignored, and the calculation is continued until the division is complete, or until a
    cycle is found in the decimal portion of the solution. If a cycle is found, the solution is
    returned with the repeated part of the solution inside brackets. """

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

    # A dictionary which holds the previous "states" of the solution. The key is the numerator,
    # and the value is the len of the decimal portion where that numerator was first found
    states = dict()

    while detect_repetition or (len(decimals) < digit_limit):
        # If the detect_repetition flag is set, keep track of previous states of the division
        # and identify when we've reached a cycle. Return the solution, with the repeated part
        # inside brackets
        if detect_repetition:
            if n not in states:
                states[n] = len(decimals)
            else:
                # starting index for the repeating part
                i = states[n]

                # extract the repeating part and the non-repeating part from the decimals, so we
                # can format the returned solution correctly
                non_repeating_part = decimals[:i]
                repeating_part = decimals[i:]
                return '{}.{}[{}]'.format(whole, non_repeating_part, repeating_part)

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
