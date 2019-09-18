import numpy as np
''' This module returns 2 values x1 and x2'''
def quad(a,b,c):
    '''This does the computing'''
    x_int_1 = (-b + np.sqrt(b**2-4*a*c))/2*a
    x_int_2 = (-b - np.sqrt(b**2-4*a*c))/2*a
    return f"The x intercepts are {x_int_1} and {x_int_2}"
