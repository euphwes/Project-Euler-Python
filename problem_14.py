"""
Longest Collatz sequence
------------------------

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proven yet (Collatz Problem), it is thought that all starting numbers
finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

from utils.timer import time_it
from utils.sequences import collatz_sequence

#-------------------------------------------------------------------------------------------------

collatz_length_dict = dict()

def get_length_of_collatz_sequence(n):
    """ Iterates through a Collatz Sequence starting with the number `n`, counting the number of
    elements along the way. When the sequence is complete, the length of the sequence starting
    with `n` is stored in a dictionary (key = starting num, value = length).num

    To improve performance, while counting the elements in the sequence, the dictionary is checked
    to see if we have previously encountered a sequence starting with the current number in the
    sequence we are currently checking. If so, we can store the current length + the length of
    the previously seen sequence, and return that. Saves us from having to fully iterate through
    the sequence if we known the length of a subsequence. """

    count = 0
    for num in collatz_sequence(n):
        if num in collatz_length_dict:
            collatz_length_dict[n] = collatz_length_dict[num] + count
            return collatz_length_dict[n]
        count += 1

    collatz_length_dict[n] = count
    return count


@time_it
def problem_14():
    f = get_length_of_collatz_sequence
    sequence_lengths = [(x, f(x)) for x in range(3,1000000)]

    # find the tuple in the list with the maximum 2nd element (the length of the sequence), and
    # print out the 1st element in that tuple (the starting value of that sequence)
    print(max(sequence_lengths, key=lambda x: x[1])[0])

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_14()
