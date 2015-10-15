"""
Longest Collatz sequence
------------------------

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proven yet (Collatz Problem), it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from utils.timer import time_it
from utils.sequences import collatz_sequence

#-------------------------------------------------------------------------------------------------

@time_it
def problem_14():
    winning_number = None
    winning_length = 0

    for x in range(3,1000000):
        length = len(list(collatz_sequence(x)))
        if length > winning_length:
            winning_length = length
            winning_number = x

    print(winning_number)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_14()
