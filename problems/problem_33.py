"""
Digit cancelling fractions
--------------------------

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to
simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and
containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of
the denominator.
"""

from utils.timer import time_it
from fractions import Fraction
from functools import reduce

#-------------------------------------------------------------------------------------------------

def false_simplify(a, b):
    """ Performs 'false simplification' on a fraction. If the numerator and denominator contain
    the same non-zero digit, remove that digit and check the value of the new fraction that is
    created. If it's the same as the original fraction, return it. Otherwise, return None. """

    # remember the original fraction
    orig_fraction = Fraction(a, b)

    # convert a and b into a list of digits. If the same non-zero digit appears in both a and b,
    # remove it from both, and set a flag which indicates that we've "simplified" this
    a, b = list(str(a)), list(str(b))
    simplified = False
    for digit in a:
        if digit != '0' and digit in b:
            simplified = True
            a.remove(digit)
            b.remove(digit)
            break

    # convert a and b back into integers
    a, b = int(''.join(a)), int(''.join(b))

    # if we didn't simplify anything, or if b == 0, return None
    if not (simplified and b):
        return None

    # Create a fraction out of the new a and b, and compare it to the old fraction
    # If they are equivalent to each other, return the Fraction to the caller.
    # Otherwise None is returned when the function terminates
    if Fraction(a, b) == orig_fraction:
        return orig_fraction


@time_it
def problem_33():
    # useful lambdas
    multiply = lambda x, y: x * y
    not_none = lambda x: x is not None

    # perform false_simplify on every number pair a, b where a and b are both 2 digits, and a < b
    potential_fractions = [false_simplify(a, b) for a in range(10, 100) for b in range(a + 1, 100)]

    # filter the list above to get only those which are not None. Get a list of Fractions
    falsly_simplified_fractions = filter(not_none, potential_fractions)

    # multiply all the fractions to get their product, and print the denominator
    # NOTE: A Fraction object always represents its numerator and denominator in smallest terms
    fraction_product = reduce(multiply, falsly_simplified_fractions)
    print(fraction_product.denominator)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_33()
