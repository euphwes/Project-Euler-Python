"""
Number spiral diagonals
-----------------------

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

def sum_diagonal_spirals(s):
    """ Returns the sum of all numbers found along the diagonals of an s×s Ulam Spiral. """

    # Determine the size of the spoke for an s×s spiral
    # A 'spoke' is a diagonal from the center to the outer corner
    # IE a 5×5 spiral has a spoke size of 3
    spoke_size = int((s - 1) / 2) + 1

    # These define the north-east and the south-west spokes, for consecutive n starting at n=0
    ne_spoke = lambda n: (2*n + 1)**2
    sw_spoke = lambda n: 4*(n**2) + 1

    # These define the north-west and the south-east spokes, for consecutive n starting at n=1
    nw_spoke = lambda n: 4*(n**2) - 6*n + 3
    se_spoke = lambda n: 4*(n**2) - 10*n + 7

    # Use a set to store the numbers, so we don't store duplicates of the center element (1)
    numbers_on_diagonal = set()

    # Calculate the numbers along each spiral using the formulas defined above, making sure we
    # start at the correct starting point for each formula
    for x in range(spoke_size):
        numbers_on_diagonal.add(ne_spoke(x))
        numbers_on_diagonal.add(sw_spoke(x))

    for x in range(1, spoke_size + 1):
        numbers_on_diagonal.add(nw_spoke(x))
        numbers_on_diagonal.add(se_spoke(x))

    return sum(numbers_on_diagonal)


@time_it
def problem_28():
    print(sum_diagonal_spirals(1001))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_28()
