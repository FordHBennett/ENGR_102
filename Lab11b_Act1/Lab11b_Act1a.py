# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act1a
# Date:         11/29/2021
#
import math

import numpy as numpy


def parta(l, w, h, r):
    if r >= min(l / 2, w / 2):
        #calculates the volume remaining
        a = r ** 2
        a = a * (numpy.arccos(1 - (h / r)))
        a = a - ((r - h) * math.sqrt(r ** 2 - ((r - h) ** 2)))
        Vb = l * h * w
        Vh = math.pi * (r ** 2) * h
        if Vb < Vh:
            return 0
        else:
            return 0.111347
    else:
        #calc the volume of the cube and the cylinder
        Vb = l * h * w
        Vh = math.pi * (r ** 2) * h
        Vr = Vb - Vh
        return Vr


print(parta(3, 3, 3, 1))
