# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act1_c.)
# Date:         7/9/2021
from math import *
print('This program calculates how much Radon-222 is left given time and initial amount')
#user input intial amount and time elapsed
t = float(input('Please enter the time (days):'))
nInitial = float(input(' Please enter the initial amount (g):'))
tHalfLife = 3.8
# radon left calc
r222Left = nInitial*2**(-t/tHalfLife)
#radon left print
print(" Radon-222 left is", '{:.2f}'.format(r222Left), "g")
