"""
Names scores
------------

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over
five-thousand first names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from utils.timer import time_it
from string import ascii_uppercase

#-------------------------------------------------------------------------------------------------

letter_dict = dict(zip(ascii_uppercase, range(1,27)))

#-------------------------------------------------------------------------------------------------

def name_list():
    """ Reads the names from the resource file, builds a list, and sorts alphabetically. """

    with open('resources/problem_022_names.txt') as f:
        return sorted((x.replace('"','') for x in next(f).split(',')))


def get_score(name, position):
    """ Returns the score for each name. The score is the name's position in the list, multiplied
    by the sum of all the letter values in the name. """

    return position * sum(letter_dict[x] for x in name)


@time_it
def problem_22():
    print(sum(get_score(name, i+1) for i, name in enumerate(name_list())))

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_22()
