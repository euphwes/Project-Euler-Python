from time import time

#-------------------------------------------------------------------------------------------------

def format_time(seconds_elapsed):
    """ Formats elapsed seconds into a human-readable string."""
    hours, remainder = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:0>2}:{:0>2}:{:05.5f}".format(int(hours), int(minutes), seconds)


def time_it(method):
    """ Simple decorator which times the function call it decorates. """

    def timed(*args, **kwargs):
        # Do an empty print here simple because I like it when there's an empty line before the
        # result is printed in the console. Makes it easier to read...
        print()

        start = time()
        result = method(*args, **kwargs)
        stop  = time()

        print('\nElapsed time: {}'.format(format_time(stop - start)))
        return result

    return timed
