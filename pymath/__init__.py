"""Main pymath module"""
from pymath import algebra
from pymath import physics
from pymath import geometry


def unitConverter(original, translated, item):
    if original == "c" and translated == "f":
        f = item * 1.8000 + 32
        print(f"{f}° F")
