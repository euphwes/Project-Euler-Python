""" Utility module for common sequences used in Project Euler. """

from itertools import islice

#-------------------------------------------------------------------------------------------------

def can_be_limited(function):
    """ Decorator which can optionally limit an otherwise infinite generator function, either by
    yielded item count or by specify a limit value.

    If `count` is specified, `count` items are yielded from the decorated generator.

    If `limit` is specified, items are yielded from the decorated generator until a value is
    reached which surpasses this limit. That item is not yielded, and the generator terminates.
    `limit` therefore specifies an inclusive upper range for the generator's values. This implies
    that we expect the values returned from the generator to be numerical values.

    NOTE: If both are specified, `count` takes precedence over `limit`."""

    def limited(*args, count=None, limit=None, **kwargs):

        gen = function(*args, **kwargs)

        if count:
            yield from islice(gen, count)

        elif limit:
            for x in gen:
                if x > limit: raise StopIteration
                yield x

        else:
            yield from gen

    return limited

#-------------------------------------------------------------------------------------------------

@can_be_limited
def fibonacci():
    """ A generator function yields which the Fibonacci Sequence. """

    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

#-------------------------------------------------------------------------------------------------

@can_be_limited
def triangle_numbers():
    """ A generator function yielding the triangle numbers. The nth triangle number is the sum
    of the natural numbers from 1 to n. """

    n = 1
    while True:
        yield sum(range(n + 1))
        n += 1

#-------------------------------------------------------------------------------------------------

def bitstrings_of_length(n):
    """ A generator function which yields all bitstrings of length `n`. """

    binary_format_string = '{' + ':0{}b'.format(n) + '}'
    binary = lambda x: binary_format_string.format(x)

    yield from (binary(x) for x in range(pow(2,n)))

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
