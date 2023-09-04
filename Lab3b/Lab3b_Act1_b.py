# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act1_b.)
# Date:         7/9/2021
from math import *
print('This program calculates the wavelength given distance and angle')
#user inputs dist and degree
distance = float(input('Please enter the distance (nm):'))
degree = float(input(' Please enter the angle (degrees):'))
#lambda calc
yambda = 2*distance*sin(radians(degree))
#lambda print
print(" Wavelength is", '{:.4f}'.format(yambda), "nm")

