"""
Prime digit replacements
------------------------

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible
values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the
first example having seven primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member
of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
with the same digit, is part of an eight prime value family.
"""

from utils.timer import time_it
from utils.primes import is_prime, get_primes_under
from utils.sequences import bitstrings_of_length

#-------------------------------------------------------------------------------------------------

def mask_value(value, mask):
    """ Takes a string input, and a mask (a bitstring of 1s and 0s) which is the same length.
    Returns a masked version of the input string, where each character that corresponds to a '1'
    in the bitstring in the same position is replaced with an asterisk. """

    masked_value = ''
    for i, char in enumerate(value):
        masked_value += char if mask[i] == '0' else '*'
    return masked_value


def get_wildcard_variants(n):
    """ A generator function which takes an input string, and yields every possible 'wildcarded'
    variant of that input. Here, a 'wildcard' variant is a modification of that input where 1
    or more characters are replaced with asterisks. Don't yield a variant that has no wildcards,
    or is composed of entirely wildcards. """

    all_wildcards = '*' * len(n)

    for mask in bitstrings_of_length(len(n)):
        wildcard_variant = mask_value(n, mask)
        if not (wildcard_variant in (n, all_wildcards)):
            yield wildcard_variant


@time_it
def problem_51():

    for prime in map(str, get_primes_under(10**6)):
        for wildcard in get_wildcard_variants(prime):

            # If the last character of a wildcard variant is a wildcard, we can eliminate it as
            # a possibility, because that wildcard will take on all even digits, making the number
            # itself even. Since we're looking for a family of 8, we can't afford to eliminate 4
            # possibilities
            if wildcard[-1] == '*':
                continue

            family = list()

            for digit in map(str, range(10)):

                # Substitute all wildcards with the digit we're currently trying
                subbed = wildcard.replace('*', digit)

                # If the first character is a 0 (by wildcard replacement), it means the integer
                # version will no longer be the same length as the input number. We can skip this
                # since we're looking for families of the same length
                if subbed[0] == '0':
                    continue

                # If the subbed number is prime, record it as a member of the family
                if is_prime(int(subbed)):
                    family.append(int(subbed))

            # After we're done with the wildcard variant, check to see if the family has 8 members
            # If so, winner winner, chicken dinner!
            if len(family) == 8:
                print(min(family))
                return

#-------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    problem_51()
