"""
Coded triangle numbers
----------------------

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first
ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and
adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 =
55 = t10. If the word value is a triangle number then we shall call theword a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly
two-thousand common English words, how many are triangle words?
"""

from utils.timer import time_it
from utils.sequences import triangle_numbers
from string import ascii_uppercase

#-------------------------------------------------------------------------------------------------

letter_dict = dict(zip(ascii_uppercase, range(1,27)))

def get_value(name):
    """ Returns the the sum of all the letter values in the name. """
    return sum(letter_dict[x] for x in name)


def word_list():
    """ Reads the words from the resource file, and returns it as a list. """
    with open('resources/problem_042_words.txt') as f:
        return list(x.replace('"','') for x in next(f).split(','))


@time_it
def problem_42():

    # get the values of all words in the list
    values = [get_value(name) for name in word_list()]

    # get all triangle numbers whose values are less than or equal to the max word score
    triangles_numbers = list(triangle_numbers(limit=max(values)))

    # get a count of word value that are triangle numbers
    print(len([x for x in values if x in triangles_numbers]))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_42()
