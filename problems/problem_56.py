"""
Powerful digit sum
------------------

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits
in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

@time_it
def problem_56():

    sums = list()
    for a in range(100):
        for b in range(100):
            sums.append(sum(int(x) for x in str(a**b)))

    print(max(sums))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_56()
