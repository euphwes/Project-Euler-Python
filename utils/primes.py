""" Utility module for working with prime numbers. """

from math import ceil, sqrt

#-------------------------------------------------------------------------------------------------

def is_prime(n):
    """ Returns whether a given number is prime. """

    if n % 2 == 0:
        return False

    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

#-------------------------------------------------------------------------------------------------

def prime_factors(n):
    """ Returns a list of the prime factors of a given number. """

    factors = list()

    while True:
        curr_factor = 2

        if is_prime(n):
            factors.append(n)
            break

        while not is_prime(curr_factor) or not n % curr_factor == 0:
            curr_factor += 1

        factors.append(curr_factor)
        n = int(n / curr_factor)

    return factors

#-------------------------------------------------------------------------------------------------

def get_first_n_primes(n):
    """ Returns a list of the first n primes. """

    primes = [2]
    curr_num = 3

    while len(primes) < n:
        if is_prime(curr_num):
            primes.append(curr_num)
        curr_num += 2

    return primes

#-------------------------------------------------------------------------------------------------

def get_nth_prime(n):
    """ Returns the nth prime number. """

    return get_first_n_primes(n).pop()
