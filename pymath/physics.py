from math import pi


def tangental_acceleration(radius, time, cycles):
    return (4 * pi**2 * radius) / (time / cycles)**2


def tangental_speed(radius, time, cycles):
    return (2*pi*radius) / (time / cycles)


def velocity(time_interval, displacement):
    return displacement/time_interval


def speed(distanse, time):
    return distanse / time


def acceleration(v1, v2, t1, t2):
    return (v2 - v1)/(t2-t1)


def displacement(initial_distance, final_distance, initial_time, final_time):
    return (final_distance-initial_distance)/(final_time-initial_time)


def force(mass, acceleration):
    return mass*acceleration
