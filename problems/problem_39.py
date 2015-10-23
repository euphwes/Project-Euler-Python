"""
Integer right triangles
-----------------------

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are
exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from utils.timer import time_it
from collections import namedtuple

#-------------------------------------------------------------------------------------------------

def triangles(n):
    """ Returns a list of tuples (a, b, c) where a, b, c are the integral length sides of a right
    triangle of perimeter n. """

    half_n = n // 2

    solutions = list()
    for a in range(1, half_n + 1):
        for b in range(a, half_n + 1):
            c = (a**2 + b**2) ** 0.5
            if a + b + c == n:
                solutions.append((a, b, int(c)))

    return solutions


@time_it
def problem_39():

    TriangleSolution = namedtuple('TriangleSolution', ['perimeter', 'solution_count'])

    # get solutions for all integer perimeters up to 1000, skipping odd perimeters
    # determined experimentally that an integral right triangle can never have an odd perimeter
    solutions = [TriangleSolution(n, len(triangles(n))) for n in range(12, 1001, 2)]

    # find the 'max' tuple by # of solutions
    best_solution = max(solutions, key=lambda x: x.solution_count)

    # display the perimeter
    print(best_solution.perimeter)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_39()
