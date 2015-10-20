"""
Coin sums
---------

In England the currency is made up of pound, £, and pence, p, and there are eight coins
in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

from utils.timer import time_it
from itertools import combinations_with_replacement

#-------------------------------------------------------------------------------------------------

@time_it
def problem_31():
    """ Calculates how many ways you can make change for £2, if you have an unlimited supply of
    the following coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).£2

    Uses a dynamic programming approach which breaks the problem down into smaller sub-problems.
    Shamelessly 'borrowed' from other sources online, since I was having trouble coming up with a
    solution myself whose runtime didn't take forever.

    Here's an example of the approach, using the case of giving change for 6p using only the
    following coins: 1p, 2p, 5p

    Initialize an array/list of zeros, the length of which is 1 larger than your target. Here,
    we'll initialize a length of array 7 and fill it with zeros. We define the first element of
    array to be 1:

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  0,  0,  0,  0,  0,  0 ]

    Since we have 1p, 2p, and 5p coins to us, we start by making change for each element in the
    array using the smallest coin available (1p). We define the number of ways for which we can
    provide change for 0p using 1p to be 1, for the sake of this algorithm.

    Now, we will make change each pence value in turn. If we make change for 1p, and give 1p (the
    coin with which we're currently working), we have 0p left. So we take the current value for 1p
    (which is 0) and add it to the current value for the remainder 0p (which is 1). 0 + 1 = 1, so
    we put 1 in the value for 1p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  0,  0,  0,  0,  0 ]

    Now, we consider making change for 2p. We give 1p (our current coin), leaving us with a
    remainder of 1p. How many ways can we give 1p using 1p coins? We look at the value in 1p,
    which is 1. We add this to the current value for 2p. 0 + 1 = 1, which we store for 2p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  1,  0,  0,  0,  0 ]

    We can keep making change for each value using the same method for the current coin (1p).
    When we are done, the array looks like this:

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  1,  1,  1,  1,  1 ]

    This makes intuitive sense. Using only a 1p coin, there is only 1 way to make change for each
    of the values above. Now that we are done counting ways to make change using the 1p coin, we
    move on to the 2p coin.

    It doesn't make sense to try to make change for 0p or 1p using the 2p coin, so we start at 2p.
    We're making change for 2p using 2p coins. We give 2p, so we have a remainder of 0p left. We
    add the value in the remainder's slot (1) to the current value that we're making change for
    (2p = 1). 1 + 1 = 2, so we store 2 for 2p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  1,  1,  1,  1 ]

    Now we make change for 3p using a 2p coin. We give 2p, leaving us with a remainder of 1p. We
    look up the value of 1p (1) and add it to the current value 1. 1 + 1 = 2, so we store 2 for 3p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  2,  1,  1,  1 ]

    Now we make change for 4p using our current coin (2p). We have 4p, give 2p, leaving us with a
    remainder of 2p. We look up the value of 2p (2) and add it to our current value (1). We store
    2 + 1 = 3 for 4p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  2,  3,  1,  1 ]

    We do the same thing for the 5p and 6p using 2p coins. We subtract a single 2p coin from the
    value we're making change for, and look up the value of the remainder, adding it to the
    current value of the amount we're making change for. When we're done with the 2p coin, our grid
    looks like this:

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  2,  3,  3,  4 ]

    Now we're onto making change using our final coin (5p). It doesn't make sense to try to make
    change for anything less than 5p using a 5p coin, so we start at 5p. We are making change for
    5p, we give a 5p coin, so our remainder is 0p. We add the value for 0p (1) to the current value.
    3 + 1 = 4, which we store for 5p.

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  2,  3,  4,  4 ]

    Now we make change for 6p using a 5p coin. We give a single 5p coin, giving us a remainder of
    1p. We look up the value for 1p (1) and add it to the current value (4). 4 + 1 = 5, which we
    store for 6p, giving us this grid:

            [pence][0p, 1p, 2p, 3p, 4p, 5p, 6p]
            [value][1,  1,  2,  2,  3,  4,  5 ]

    Now we have completed making change for every value up to 6p, using 1p, 2p, and 5p coins.

    The answer to our question (how many ways can make change for 6p using 5p, 2p, and 1p coins?)
    is the value currently stored for 6p. There are 5 ways to make change for 6p using 1p, 2p, and
    5p coins.

    This algorithm can be used for any target amount, with any denomination of coins available.
    """

    goal  = 200
    coins = (1, 2, 5, 10, 20, 50, 100, 200)

    ways = [1] + [0 for _ in range(goal)]

    for coin in coins:
        for i in range(coin, goal + 1):
            ways[i] += ways[i - coin]

    print(ways[-1])

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_31()
