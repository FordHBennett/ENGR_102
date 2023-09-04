#By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 2b(Lab2b_Act2c.)
# Date:         7/9/2021
from math import *
t1 = 30
t2 = 60
counterFifth = (t2 -t1)/4
counter = t1
def interpolation(t):
    x1 = 2
    x2 = 25
    x0 = 0
    x0 = (x2 - x1)/(85 - 12)
    x0 = x0*(t-12)
    x0 = x0 + x1
    print('At time', counter, 'seconds:')
    print("x0 =", x0, "m")

    y1 =3
    y2 = -5
    y0 = 0
    y0 = (y2 - y1)/(85 - 12)
    y0 = y0*(t-12)
    y0 = y0 + y1
    print("y0 =", y0, "m")

    z1 = 7
    z2 = 11
    z0 = 0
    z0 = (z2 - z1)/(85 - 12)
    z0 = z0*(t-12)
    z0 = z0 + z1
    print("z0 =", z0, "m")
    if counter < t2:
        print("----------------------")

for i in range(5):
    interpolation(counter)
    counter = counter + counterFifth
