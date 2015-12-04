"""
Spiral primes
-------------

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side
length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is
more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is,
a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9
will be formed. If this process is continued, what is the side length of the square spiral for
which the ratio of primes along both diagonals first falls below 10%?
"""

from utils.timer import time_it
from utils.primes import is_prime

from itertools import count

#-------------------------------------------------------------------------------------------------

@time_it
def problem_58():

    # These define the north-east and the south-west spokes, for consecutive n starting at n=0
    ne_spoke = lambda n: (2*n + 1)**2
    sw_spoke = lambda n: 4*(n**2) + 1

    # These define the north-west and the south-east spokes, for consecutive n starting at n=1
    nw_spoke = lambda n: 4*(n**2) - 6*n + 3
    se_spoke = lambda n: 4*(n**2) - 10*n + 7

    all_spoke_values = set()
    prime_spoke_values = set()

    for n in count(0):
        for value in (ne_spoke(n), sw_spoke(n), nw_spoke(n+1), se_spoke(n+1)):
            all_spoke_values.add(value)
            if is_prime(value):
                prime_spoke_values.add(value)

        if n > 1 and (len(prime_spoke_values) / len(all_spoke_values)) < 0.10:
            spiral_side_length = 2*n + 1
            print(spiral_side_length)
            break

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_58()
