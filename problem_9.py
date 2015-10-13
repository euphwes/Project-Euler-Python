"""
Special Pythagorean triplet
---------------------------

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from utils.timer import timeit

#-------------------------------------------------------------------------------------------------

def is_pythagorean_triplet(a,b,c):
    """ Determine if the provided arguments form a Pythagorean triplet: a^2 + b^2 == c^2 """
    return pow(a,2) + pow(b,2) == pow(c,2)


@timeit
def problem_9():
    for a in range(3, 500):
        for b in range(3, 500):
            c = 1000 - a - b
            if is_pythagorean_triplet(a,b,c) and (a + b + c == 1000):
                print(a*b*c)
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    print()
    problem_9()
