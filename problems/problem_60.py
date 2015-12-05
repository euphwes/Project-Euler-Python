"""
Prime pair sets
---------------

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and
1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four
primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce
another prime.
"""

from utils import memoize
from utils.timer import time_it
from utils.primes import is_prime, get_primes_under

from itertools import combinations, product

#-------------------------------------------------------------------------------------------------

@memoize
def concats_to_prime(p1, p2):
    """ Check if both concatenations of primes p1 and p2 (p1+p2, and p2+p1), form a prime. """

    p1, p2 = str(p1), str(p2)
    t1, t2 = int(p1 + p2), int(p2 + p1)
    return all(is_prime(t) for t in (t1, t2))


@time_it
def problem_60():

    # get list of primes, discard 2
    primes = list(get_primes_under(9000))
    primes.pop(0)

    for a in primes:

        # build up a list of primes which pair with `a` to concatenate and form other primes
        pairs_with_a = list()
        for b in primes:
            if a == b: continue
            if concats_to_prime(a, b):
                pairs_with_a.append(b)

        # For every combination of 4 in the primes which pair with `a`:
        #     if every pair of them also concats_to_prime, we found the winner!
        # 
        # We know the first result obtained must be the correct answer, since combinations()
        # yield combos in lexographical order, so we'll get combos with smaller numbers first
        for combo in combinations(pairs_with_a, 4):
            if all(concats_to_prime(p1, p2) for p1, p2 in product(combo, repeat=2) if p1 != p2):
                print(sum(combo) + a)
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_60()
