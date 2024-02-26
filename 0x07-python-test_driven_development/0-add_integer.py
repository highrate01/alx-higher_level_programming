#!/usr/bin/python3

def add_integer(a, b=98):
    """Return result of the addition a snd b
    Notes: float values are converted/typecasted to int before used
    Rease TypeError if either a or b is not an inetger
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
