"""
Summation of primes
-------------------

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from utils.timer import time_it
from utils.primes import get_primes_under

#-------------------------------------------------------------------------------------------------

@time_it
def problem_10():
    print(sum(get_primes_under(2000000)))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_10()
