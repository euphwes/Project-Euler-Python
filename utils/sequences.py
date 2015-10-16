""" Utility module for common sequences used in Project Euler. """

#-------------------------------------------------------------------------------------------------

def bitstrings_of_length(n):
    """ A generator function which yields all bitstrings of length `n`. """

    binary_format_string = '{' + ':0{}b'.format(n) + '}'
    binary = lambda x: binary_format_string.format(x)

    yield from (binary(x) for x in range(pow(2,n)))

#-------------------------------------------------------------------------------------------------

def triangle_numbers():
    """ A generator function yielding the triangle numbers. The nth triangle number is the sum
    of the natural numbers from 1 to n. """

    n = 1
    while True:
        yield sum(range(n + 1))
        n += 1

#-------------------------------------------------------------------------------------------------

def collatz_sequence(n):
    """ A generator function yielding the Collatz Sequence. The sequence follows this pattern:
            n → n/2 (n is even)
            n → 3n + 1 (n is odd) """

    while True:

        yield n

        if n == 1:
            raise StopIteration

        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3*n + 1)
