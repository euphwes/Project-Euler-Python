""" General-purpose utility functions can go here, which don't necessarily go better
anywhere else. """

#-------------------------------------------------------------------------------------------------

# Convert a decimal integer to binary. Remove leading '0b' and just return bitstring.
# Ensure the argument is a decimal integer. This will work on ints and strings.
binary = lambda n: bin(int(n))[2:]

# Returns whether or not a value is a palindome. Coerce the argument to a string. This will work
# on ints and strings
is_palindome = lambda n: str(n) == ''.join(reversed(str(n)))

#-------------------------------------------------------------------------------------------------

def is_0_9_pandigital(n):
    """ Returns True if the n contains every digit 0-9 exactly once, or False otherwise. Ensure n
    is a string first. Works on ints and strings. """
    n = str(n)
    return (len(n) == 10) and (set('1234567890') == set(n))


def is_n_digit_pandigital(value, n):
    """ Returns True if `value` contains every digit 1-n exactly once, or False otherwise. Ensure
    `value` is a string first. Works on ints and strings. """
    value = str(value)
    return (len(value) == n) and (set('123456789'[:n]) == set(value))


def is_pandigital(n):
    """ Returns True if the n contains every digit 1-9 exactly once, or False otherwise. Ensure n
    is a string first. Works on ints and strings. """
    return is_n_digit_pandigital(n, 9)

#-------------------------------------------------------------------------------------------------
