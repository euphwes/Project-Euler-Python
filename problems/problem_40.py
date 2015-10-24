"""
Champernowne's constant
-----------------------

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from utils.timer import time_it
from utils.sequences import champernownes_constant

#-------------------------------------------------------------------------------------------------

@time_it
def problem_40():
    answer = 1
    for i, digit in enumerate(champernownes_constant(count=1000000)):
        if (i+1) in (1, 10, 100, 1000, 10000, 100000, 1000000):
            answer *= int(digit)

    print(answer)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_40()
