"""
Permuted multiples
------------------

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from utils.timer import time_it
from itertools import count

#-------------------------------------------------------------------------------------------------

@time_it
def problem_52():

    matches = lambda x, y: len(x) == len(y) and set(x) == set(y)

    for x in count(123456):
        if not all(matches(str(2*x), str(y)) for y in (3*x, 4*x, 5*x, 6*x)):
            continue

        print(x)
        break

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_52()
