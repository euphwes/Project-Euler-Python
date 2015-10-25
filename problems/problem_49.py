"""
Prime permutations
------------------

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is
unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this
property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from utils.timer import time_it
from utils.primes import get_primes_under

#-------------------------------------------------------------------------------------------------

@time_it
def problem_49():

    # get a generator of primes under 10k (since we know the primes in question are 4 digits)
    # and then discard all 3-digit ones
    primes = get_primes_under(10**4)
    while next(primes) < 999:
        pass

    # turn the remainder of the primes in the generator into a list
    primes = list(primes)

    for p in primes:
        if p in (1487, 4817, 8147):
            # skip this one since the problem is asking for the other one
            continue

        # get the digits of the current prime in sorted order, and get any other primes
        # in the list which contain exactly the same digits
        sorted_digits = sorted(str(p))
        others = [x for x in primes if x != p and sorted(str(x)) == sorted_digits]

        # if we don't have at least 2 other primes with the same digits, skip to the next prime
        if len(others) < 2:
            continue

        # check each pair of primes in the `others` list, and if the difference between them is
        # the same as the difference between our current prime and the first of these, we have
        # a winner
        for n1 in others:
            for n2 in [x for x in others if x > n1]:
                if (n2 - n1) == (n1 - p):
                    print('{}{}{}'.format(p, n1, n2))
                    return


#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_49()
