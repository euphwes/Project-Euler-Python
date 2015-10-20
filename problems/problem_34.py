"""
Digit factorials
----------------

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from utils.timer import time_it
from math import factorial

#-------------------------------------------------------------------------------------------------

# Pre-calculate the factorials of digits 0 - 9, so we don't have to keep recalculating those
# every time in num_equals_sum_of_digit_factorials below
factorials_dict = dict(zip(range(10), [factorial(x) for x in range(10)]))

#-------------------------------------------------------------------------------------------------

def num_equals_sum_of_digit_factorials(n):
    """ Return True if a given numer n is equal to the sum of the factorials of its digits. """
    digit_factorial_sum = 0
    for digit in str(n):
        digit_factorial_sum += factorials_dict[int(digit)]

    return digit_factorial_sum == n


@time_it
def problem_34():
    # Note: this upper limit of 10^5 was determined experimentally. There is probably a clever
    # mathematical way to determine it, but I haven't found it yet
    print(sum(filter(num_equals_sum_of_digit_factorials, range(3, 10**5))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_34()
