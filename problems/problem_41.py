"""
Pandigital prime
-----------------

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from utils.primes import is_prime
from utils.timer import time_it
from itertools import permutations

#-------------------------------------------------------------------------------------------------

@time_it
def problem_41():

    # utility lambda to turn a tuple of digits into an integer
    make_int = lambda x: int(''.join(x))

    # start with 9 digits, then work our way down, so we're starting with the largest
    for n in reversed(range(1, 10)):

        # Since permutations() will yield in lexicographic order, we can reverse the digit
        # sequence we feed it and we will know that each permutation will be smaller than the last.
        # Therefore, the very first prime that we find will be the answer
        digits = reversed('123456789'[:n])
        for n in (make_int(x) for x in permutations(digits)):
            if is_prime(n):
                print(n)
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_41()
