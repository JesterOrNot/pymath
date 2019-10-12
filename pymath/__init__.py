"""Main pymath module"""
import pymath.algebra
import pymath.physics
import pymath.geometry
import pymath.chemistry
import pymath.misc
def unitConverter(original,translated):
    if original == "c" and translated == "f":
        f = original * 1.8000 + 32
        print(f"{f}° F")
