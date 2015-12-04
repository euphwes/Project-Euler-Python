"""
Square root convergents
-----------------------

It is possible to show that the square root of two can be expressed as an infinite
continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985,
is the first example where the number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits
than the denominator?
"""

from utils import memoize
from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

@memoize
def A001333(n):
    """ OEIS.org A001333: The numerators of the nth iteration of the continued fraction convergent
    to the square root of 2. """

    if n in (0, 1):
        return 1

    return 2*A001333(n-1) + A001333(n-2)


@memoize
def A000129(n):
    """ OEIS.org A000129: The denominators of the nth iteration of the continued fraction
    convergent to the square root of 2. """

    if n in (0, 1):
        return n

    return 2*A000129(n-1) + A000129(n-2)


@time_it
def problem_57():

    # Start at n=2 because A001333 and A000129 start with 1, 1 and 0, 1 respectively.
    # As defined by Project Euler, the first iteration of that continued fraction is 3/2, which
    # are terms n=2 of those sequences
    satisfies_criteria = lambda n: len(str(A001333(n+2))) > len(str(A000129(n+2)))

    print(len(list(filter(satisfies_criteria, range(1000)))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_57()
