# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act1_a.)
# Date:         7/9/2021
from math import *
print('This program calculates the applied force given mass and acceleration')
#user inputs the mass and acc
mass = float(input('Please enter the mass (kg):'))
acceleration = float(input(' Please enter the acceleration (m/s^2):'))
#force calc
force = mass*acceleration
#force print
print(" Force is", '{:.1f}'.format(force), "N")

