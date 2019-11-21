from math import sqrt
from math import pi


def circumference(diameter):
    """Function that computes circumference."""
    circumference = pi * diameter
    return circumference


def pythag_theor(a, b):
    c = sqrt(a**2 + b**2)
    return c
def area_of_circle(radius):
    area = pi * radius**2
    return area
def area_of_trap(b1, b2, h):
    equ = ((b1+b2)/2)*h
    return equ
def area_of_triangle(base, height):
    equ = 1/2*base*height
    return equ
