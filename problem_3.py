"""
Largest prime factor
--------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from utils.timer import time_it
from utils.primes import prime_factors

#-------------------------------------------------------------------------------------------------

@time_it
def problem_3():
    print(max(prime_factors(600851475143)))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_3()
