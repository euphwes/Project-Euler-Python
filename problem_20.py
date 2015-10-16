"""
Factorial digit sum
-------------------

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from utils.timer import time_it
from math import factorial

#-------------------------------------------------------------------------------------------------

@time_it
def problem_20():
    print(sum(int(x) for x in str(factorial(100))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_20()
