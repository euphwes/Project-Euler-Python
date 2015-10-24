"""
Pentagon numbers
----------------

Pentagonal numbers are generated by the formula Pn=n(3n−1)/2. The first 10 pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48,
is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
and D = |Pk − Pj| is minimised; what is the value of D?
"""

from utils.timer import time_it
from utils.sequences import pentagonal_numbers, is_pentagonal

#-------------------------------------------------------------------------------------------------

@time_it
def problem_44():

    # upper limit determined experimentally. Haven't found an analytical way to determine it
    pentagonals = list(pentagonal_numbers(count=3000))

    candidates = list()
    for a in pentagonals:
        for b in pentagonals:
            if a == b:
                continue
            if is_pentagonal(abs(a - b)) and is_pentagonal(a + b):
                # the first such pair we find should be smallest difference, so we can finish
                print(abs(a - b))
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_44()