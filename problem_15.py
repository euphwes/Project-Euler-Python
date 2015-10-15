"""
Lattice paths
--------------

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

from utils.timer import time_it
from math import factorial

#-------------------------------------------------------------------------------------------------

@time_it
def problem_15():
    """ Using the 2x2 grid as an example:

    To reach the bottom-right corner from the top-left corner, only being able to move right and
    down, 1 unit at a time, you must have to move right twice, and down twice, but not necessarily
    in that order. The following paths are valid (where R = right, and D = down):

    RRDD, RDDR, RDRD, DDRR, DRRD, DRDR

    These are distinct permutations of the letters DDRR. To find these, we find the total number
    of permutations of these 4 letters (4!) and then divide by the number of permutations of the
    repeated letters (2! each for R and D).

    For the case of a 20x20 grid, simply the number of distinct permutations of 20 Ds, and 20 Rs.
    """
    
    x, y = 20, 20
    number_paths = int(factorial(x + y)/(factorial(x) * factorial(y)))
    print(number_paths)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_15()
