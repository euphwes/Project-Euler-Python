"""
Reciprocal cycles
-----------------

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

from utils.timer import time_it
from utils.math import long_divison

#-------------------------------------------------------------------------------------------------

@time_it
def problem_26():
    best_repeating_length = 0
    winning_denominator = None

    for denominator in range(1, 1000):
        result = long_divison(1, denominator, detect_repetition=True)

        # if '[' is in the result, we know there was a repeating portion
        if '[' in result:

            # get the indices where we should slice the result string to get the substring inside
            # the brackets (aka the repeating portion)
            i, j = result.find('[') + 1, result.find(']')

            repeating = result[i:j]

            if len(repeating) > best_repeating_length:
                best_repeating_length = len(repeating)
                winning_denominator = denominator

    print(winning_denominator)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_26()
