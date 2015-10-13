"""
10001st prime
-------------

By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from utils.timer import time_it
from utils.primes import get_nth_prime

#-------------------------------------------------------------------------------------------------

@time_it
def problem_7():
    print(get_nth_prime(10001))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_7()
