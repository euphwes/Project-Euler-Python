"""
Truncatable primes
-------------------

The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and
right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from utils.timer import time_it
from utils.primes import get_primes_under, is_prime

#-------------------------------------------------------------------------------------------------

def is_truncatable(n):
    """ Returns True if the provided prime number remains prime after its digits are truncated
    both from the left and from the right, and it remains prime at every step. """

    if any(x in str(n) for x in ('4', '6', '8')):
        return False

    # Utility lambda to turn a list of digit characters back into an int
    make_int = lambda x: int(''.join(x))

    # Make two copies of lists of the digits of n, one each for testing truncation from the 
    # left and from the right
    test_right = list(str(n))
    test_left  = list(str(n))

    # Keep popping a digit off the left and off the right, and testing if the new numbers are
    # prime. If any are not, return False
    for _ in range(len(str(n)) - 1):
        test_right.pop()
        test_left.pop(0)
        if not is_prime(make_int(test_right)) or not is_prime(make_int(test_left)):
            return False

    # If we get here, the prime is fully truncatable both from left and from right
    return True


@time_it
def problem_37():
    
    truncatables = list()

    # Get a list of primes under 10^6, and discard the first four (2, 3, 5, and 7) since those
    # don't count as truncatable since they are single-digit. Upper limit of 10^6 was determined
    # experimentally
    primes = get_primes_under(10**6)
    for _ in range(4):
        next(primes)

    # Keep checking primes if they're truncatable, and if they are, append them to the list
    # Stop once we hit 11 primes in the list, since the problem description tells us there are
    # only 11 of them
    while len(truncatables) < 11:
        n = next(primes)
        if is_truncatable(n):
            truncatables.append(n)

    print(sum(truncatables))

#------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_37()
