"""
Double-base palindromes
-----------------------

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

from utils import is_palindome, binary
from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

@time_it
def problem_36():
    double_palindrome = lambda n: is_palindome(n) and is_palindome(binary(n))
    print(sum(filter(double_palindrome, range(10**6))))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_36()
