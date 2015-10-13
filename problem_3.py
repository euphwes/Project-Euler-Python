"""
Largest prime factor
--------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from utils.timer import timeit
from utils.primes import prime_factors

#-------------------------------------------------------------------------------------------------

@timeit
def problem_3():
    print(max(prime_factors(600851475143)))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print()
    problem_3()
