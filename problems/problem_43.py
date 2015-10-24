"""
Sub-string divisibility
-----------------------

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the
digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility
property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4 = 406 is divisible by 2
d3d4d5 = 063 is divisible by 3
d4d5d6 = 635 is divisible by 5
d5d6d7 = 357 is divisible by 7
d6d7d8 = 572 is divisible by 11
d7d8d9 = 728 is divisible by 13
d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from utils.timer import time_it
from itertools import permutations

#-------------------------------------------------------------------------------------------------

@time_it
def problem_43():

    # a list of tuples, where the first element of each tuple is the start index for the numbers'
    # substrings, and the second element is the number which it must be divisible by
    divisibility_requirements = [
        (2,2),
        (3,3),
        (4,5),
        (5,7),
        (6,11),
        (7,13),
        (8,17),
    ]

    meets_requirements = list()

    # check each permutation of 1234567890. These will all be 0-9 pandigital numbers
    for perm in permutations('1234567890'):

        # make the permutation into a string again
        perm = ''.join(perm)

        # check that each substring is divisible by the paired prime. If any are not, break this
        # inner for-loop
        for i, div in divisibility_requirements:
            n = int(perm[i-1:i+2])
            if n % div != 0:
                break
        else:
            # if this clause is hit, it's because the for loop was not broken. This means all
            # divisibility requirements were met, so we can save this number
            meets_requirements.append(int(perm))

    print(sum(meets_requirements))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_43()
