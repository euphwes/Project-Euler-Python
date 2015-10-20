"""
Pandigital products
-------------------

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as 
1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in
your sum.
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

def is_pandigital(test):
    """ Returns True if the argument contains every digit 1-9 exactly once, or False otherwise."""
    return (len(test) == 9) and (set('123456789') == set(test))


@time_it
def problem_32():
    # Build up the list of product candidates. We know that the total number of digits across all
    # solutions must be 9 digits, so we can exclude:
    #
    # a * b = cdefghi  -- since the max we can get is 9 * 8, which doesn't have 7 digits
    # a * bc = defghi  -- since the max we can get is 98 * 7, which doesn't have 6 digits
    # ab * cd = efghi  -- since the max we can get is 98 * 76, which doesn't have 5 digits
    # etc
    #
    # We can limit to the following forms, since these are the only ways to get 9 digits total:
    # a * bcde = fghi
    # ab * cde = fghi
    #
    products = list()
    products.extend([(a, b, a*b) for a in range(1,10) for b in range(1000,10000)])
    products.extend([(a, b, a*b) for a in range(10,100) for b in range(100,1000)])

    pandigital_products = {c for a, b, c in products if is_pandigital('{}{}{}'.format(a,b,c))}
    print(sum(pandigital_products))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_32()
