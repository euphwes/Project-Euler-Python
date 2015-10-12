from time import time

#-------------------------------------------------------------------------------------------------

def format_time(seconds_elapsed):
    """ Formats elapsed seconds into a human-readable string."""
    hours, remainder = divmod(seconds_elapsed, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:0>2}:{:0>2}:{:05.5f}".format(int(hours), int(minutes), seconds)


def timeit(method):
    """ Simple decorator which times the function call it decorates. """

    def timed(*args, **kwargs):
        start = time()
        result = method(*args, **kwargs)
        stop  = time()

        print('\nElapsed time: {}'.format(format_time(stop - start)))
        return result

    return timed
