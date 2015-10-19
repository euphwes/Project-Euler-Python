"""
Digit fifth powers
------------------

Surprisingly there are only three numbers that can be written as the sum of fourth powers
of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

def sum_of_nth_power_of_digits(num, power):
    return sum(int(n)**power for n in str(num))


@time_it
def problem_30():

    # The power to which we'll raise each digit, 
    # and the maximum value a single digit raised to that power can be
    x = 5
    max_per_digit = 9**x

    # Determine the upper limit of numbers we need to check by figuring out what point the
    # largest n-digit number is greater than (n * max_per_digit)
    digit_limit = 2
    while (10**digit_limit - 1) <= (digit_limit * max_per_digit):
        digit_limit += 1

    # Finally, get the answer
    matches_digit_sum = lambda i: i == sum_of_nth_power_of_digits(i, x)

    print(sum(filter(matches_digit_sum, range(10, 10**digit_limit))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_30()
