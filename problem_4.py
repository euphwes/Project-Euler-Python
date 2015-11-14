"""
Largest palindrome product
--------------------------

A palindromic number reads the same both ways. The largest palindrome made from the product of two
2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

def is_palindome(val):
    """ Returns whether or not a value is a palindome. For non-string arguments, they are first
    converted to their string representation. """

    if type(val) is not str:
        val = str(val)
    return val == ''.join(reversed(val))


@time_it
def problem_4():
    three_digit_products = (int(x * y) for x in range(100,1000) for y in range(100,1000))
    palindrome_products = filter(is_palindome, three_digit_products)
    print(max(palindrome_products))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_4()
