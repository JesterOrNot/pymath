import math
import cmath


def log(base, awnser):
    """Solves logarithms."""
    if awnser == 1:
        return 0
    if base < 0 and awnser > 0:
        return "Error: can not happen"
    result = 0
    exponent = 0
    while result != awnser:
        exponent += 1
        result = base**exponent
        if result == awnser:
            return exponent


def quad(a, b, c):
    """Compute the equation."""
    try:
        x_int_1 = (-b + math.sqrt(b**2-4*a*c))/2*a
    except ValueError:
        x_int_1 = (-b + cmath.sqrt(b**2-4*a*c))/2*a
    try:
        x_int_2 = (-b - math.sqrt(b**2-4*a*c))/2*a
    except ValueError:
        x_int_2 = (-b + cmath.sqrt(b**2-4*a*c))/2*a
    return x_int_1, x_int_2
