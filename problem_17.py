"""
Number letter counts
--------------------

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many
letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""

from utils.timer import time_it

#-------------------------------------------------------------------------------------------------

# except zero, since we dont' say "zero", letter lengths of:
# zero, one, two, three, four, five, six, seven, eight, nine
ones_dict = dict(zip(range(10), [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]))

# letter lengths of:
# ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
teens_dict = dict(zip(range(10), [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]))

# letter lengths of:
# twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
tens_above_1_dict = dict(zip(range(2,10), [6, 6, 5, 5, 5, 7, 6, 6]))

# letters lengths of:
# one hundred, two hundred, three hundred, four hundred, etc
# `hundred` is 7 letters, + the length of the ones which preceed the it
hundreds_dict = {n: ones_dict[n] + 7 for n in range(10)}

def calculate_letter_count(ones, tens, hundreds):
    """ Calculate the number of letters used in spelling out the word representation of the number
    provided. Omits spaces and hyphens. """

    # less than 10, return just ones count
    if (not tens) and (not hundreds):
        return ones_dict[ones]

    # somewhere in the teens
    if (not hundreds) and (tens == 1):
        return teens_dict[ones]

    # greater than teens, but less than 100
    if (tens > 1) and (not hundreds):
        return ones_dict[ones] + tens_above_1_dict[tens]

    # if somewhere in the 100s
    if hundreds:
        # even multiple of 100, meaning no "and"
        if (not tens) and (not ones):
            return hundreds_dict[hundreds]

        # somewhere in the 100s, with 10s and/or 1s
        # get 100s letter count + "and" + recursively count the letters of the non-hundreds part
        else:
            return hundreds_dict[hundreds] + 3 + calculate_letter_count(ones, tens, 0)


@time_it
def problem_17():
    letter_count = 0
    for hundreds in range(10):
        for tens in range(10):
            for ones in range(10):
                # we're not counting zero, so skip that
                if ones + tens + hundreds == 0:
                    continue
                letter_count += calculate_letter_count(ones, tens, hundreds)

    letter_count += len('onethousand')
    print(letter_count)

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_17()
