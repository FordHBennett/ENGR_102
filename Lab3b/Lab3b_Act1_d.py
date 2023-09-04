# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act1_d.)
# Date:         21/9/2021
from math import *
print('This program calculates the pressure given moles, volume, and temperature')
#user inputs moles, volume and temp
n = float(input('Please enter the number of moles:'))
volume = float(input(' Please enter the volume (m^3):'))
temp = float(input(' Please enter the temperature (K):'))
gasConstant = 8.314
#pressure calc
p = (gasConstant*n*temp)/volume / 1000
#p = int(p)
#pressure print
print(" Pressure is", '{:.0f}'.format(p), "kPa")

