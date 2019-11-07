"""Returns a tuple with 2 values x1 and x2."""
import math
import cmath


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
