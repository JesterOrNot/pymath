import pymath
radius = float(input())
time = float(input())
cycles = float(input())
print("tangental acceleration = {}".format(pymath.physics.tangental_acceleration(radius, time, cycles)))
