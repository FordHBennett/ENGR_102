# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 2b(Lab2b_Act1.)
# Date:         7/9/2021
from math import *

mass = 2
acceleration = 5
print("Force is", mass*acceleration, "N")

distance = .025
degree = 25
print("Wavelength is", 2*distance*sin(radians(degree)), "nm")

nInitial = 3
t = 5
tHalfLife = 3.8
print("Radon-222 left is", nInitial*2**(-t/tHalfLife), "g")

temp = 425
n = 5
gasConstant = 8.314
volume = .15*1000
print("Pressure is", (gasConstant*n*temp)/volume, "kPa")

