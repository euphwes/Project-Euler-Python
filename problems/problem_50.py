"""
Consecutive prime sum
---------------------

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms,
and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from utils.timer import time_it
from utils.primes import get_primes_under, is_prime

from itertools import count

#-------------------------------------------------------------------------------------------------

@time_it
def problem_50():

    limit = 10**6

    # find the smallest list of primes which will sum up to at least the limit we set above
    for x in count(1):
        primes = list(get_primes_under(10**x))
        if sum(primes) > limit:
            break

    # starting with the longest possible sequence (every element in the list), and then working
    # to smaller sequence lengths
    for length in reversed(range(1, len(primes) + 1)):

        # Use a "sliding window" approach. Starting at the low end of the list, grab the first
        # `length` elements and check it. Then slide the window right 1 element, and grab those,
        # and check it, etc
        for start in range(len(primes)-length):
            candidate = sum(primes[start:start+length])

            # if the candidate sum is bigger than the limit, no point in checking any more windows
            # of size `length`. Break the inner loop, and reduce the length
            if candidate >= limit:
                break

            # if the candidate sum is prime, we're done!
            if is_prime(candidate):
                print(candidate)
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_50()
