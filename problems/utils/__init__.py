""" General-purpose utility functions can go here, which don't necessarily go better
anywhere else. """

#-------------------------------------------------------------------------------------------------

def is_palindome(val):
    """ Returns whether or not a value is a palindome. For non-string arguments, they are first
    converted to their string representation. """

    if type(val) is not str:
        val = str(val)
    return val == ''.join(reversed(val))

