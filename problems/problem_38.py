"""
Pandigital multiples
--------------------

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the
pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated
product of an integer with (1,2, ... , n) where n > 1?
"""

from utils import is_pandigital
from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

def concatenated_product(n):
    """ Calculates the 'concatenated product' of n as defined in the problem description above.
    Makes sure that the concatenated product is at least 9 digits, so there it is a candidate for
    being pandigital. """

    # start off with the digits of n
    digits = str(n)

    # concatenate the digits of n * x, where x = 2, 3, 4 ...
    x = 2
    while len(digits) < 9:
        digits += str(n*x)
        x += 1

    # return the number itself
    return int(digits)


@time_it
def problem_38():
    # Get a list of concatenated products from n=1 to n=10^4 (upper limit established
    # experimentally), and filter so only the pandigital numbers remain. Sort them so the largest
    # is the last item, and pop that.
    candidates = [concatenated_product(n) for n in range(10**4)]
    candidates = sorted(filter(is_pandigital, candidates))
    print(candidates.pop())

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_38()
