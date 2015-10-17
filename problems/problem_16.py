"""
Power digit sum
---------------

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

@time_it
def problem_16():
    print(sum(int(x) for x in str(pow(2,1000))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_16()
