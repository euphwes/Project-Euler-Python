""" Utility module for common sequences used in Project Euler. """

#-------------------------------------------------------------------------------------------------

def triangle_numbers():
    """ A generator function yielding the triangle numbers. The nth triangle number is the sum
    of the natural numbers from 1 to n. """

    n = 1
    while True:
        yield sum(range(n + 1))
        n += 1
