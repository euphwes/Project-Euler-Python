"""
Smallest multiple
-----------------

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from utils.timer import timeit

#-------------------------------------------------------------------------------------------------

@timeit
def problem_5():
    not_factors_of_20_below_20  = list(reversed((3,6,7,8,9,11,12,13,14,15,16,17,18,19)))
    is_not_mult_of_all_below_20 = lambda x: any(x % y != 0 for y in not_factors_of_20_below_20)

    num = 20
    while True:
        if is_not_mult_of_all_below_20(num):
            num += 20
        else:
            print(num)
            break

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print()
    problem_5()
