from math import pi


def tangental_acceleration(radius, time, cycles):
    awns = (4 * pi**2 * radius) / (time / cycles)**2
    return awns


def tangental_speed(radius, time, cycles):
    awns = (2*pi*radius) / (time / cycles)
    return awns


def velocity(time_interval, displacement):
    velocity = displacement/time_interval
    return velocity


def speed(distanse, time):
    equ = distanse / time
    return equ


def acceleration(v1, v2, t1, t2):
    acceleration = (v2 - v1)/(t2-t1)
    return acceleration


def displacement(initial_distance, final_distance, initial_time, final_time):
    equation = (final_distance-initial_distance)/(final_time-initial_time)
    return equation
