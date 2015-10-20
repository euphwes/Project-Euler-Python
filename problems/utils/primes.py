""" Utility module for working with prime numbers. """

from math import ceil, sqrt

#-------------------------------------------------------------------------------------------------

def is_prime(n):
    """ Returns whether a given number is prime. """

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for x in range(3, int(sqrt(n)) + 1, 2):
        if n % x == 0:
            return False

    return True

#-------------------------------------------------------------------------------------------------

def prime_factors(n):
    """ Returns a list of the prime factors of n. """

    factors = list()

    test = 2
    while test <= n:
        if n % test == 0:
            n /= test
            factors.append(test)
        else:
            if test == 2:
                test += 1
            else:
                test += 2

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

#-------------------------------------------------------------------------------------------------

def get_primes_under(limit):
    """ A generator implementing the Sieve of Erasthones, yielding all primes under `limit`. """

    # Initialize the list with bools indicating whether the nth element is prime or not
    # 0, 1 are not primes, 2 is prime, and from there we assume the rest are prime until we
    # identify it as a multiple of an already-returned prime
    prime_candidates = [False, False] + ([True] * (limit-2))

    for num, is_prime in enumerate(prime_candidates):
        if is_prime:
            yield num

            # after we yield a number we know is prime, mark all multiples of it as non-prime
            # so we don't return those
            for i in range(num*num, limit, num):
                prime_candidates[i] = False
