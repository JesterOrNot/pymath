import numpy as np
def quadraticEqu(a,b,c):
    x_int_1 = (-b + np.sqrt(b**2-4*a*c))/2*a
    x_int_2 = (-b - np.sqrt(b**2-4*a*c))/2*a
    return f"The x intercepts are {x_int_1} and {x_int_2}"