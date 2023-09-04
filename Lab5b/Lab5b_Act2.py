# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act1_a.)
# Date:         10/5/2021
#gets users stress
xUser = float(input('Enter the strain: '))
# Calcs equation from 0 to .01
def function1(x1):
    x2 = .01
    if(x1 != x2):
        slope = (43 - 0)/(x2 - 0)
        function = slope*(x1-0) + 0
        return function
    else:
        return 43.0
# Calcs equation from .01 to .06

def function2(x1):
    x2 = .06
    if (x1 != x2):
        slope = (43.5 - 43)/(x2 - .01)
        function = slope*(x1-.01) + 43
        return function
    else:
        return 43.5

# Calcs equation from .06 to .18
def function3(x1):
    x2 = .18
    if (x1 != x2):
        slope = (60 - 43.5)/(x2 - .06)
        function = slope*(x1-.06) + 43.5
        return function
    else:
        return 60.0

# Calcs equation from .18 to .27
def function4(x1):
    x2 = .27
    if (x1 != x2):
        slope = (51 - 60)/(x2 - .18)
        function = slope*(x1-.18) + 60
        return function
    else:
        return 51.0
# if x is less than 0 then that is an invalid number
if(xUser < 0):
    print('Strain is undefined in that region')

if(xUser == 0):
    print('The stress is approximately', 0.0)
# if x is between 0 and .01
if(xUser > 0 and xUser <= .01):
    print('The stress is approximately', function1(xUser))
# if x is between .06 and .06
if(xUser > .01 and xUser <= .06):
    print('The stress is approximately', function2(xUser))
# if x is between .06 and .18
if(xUser > .06 and xUser <= .18):
    print('The stress is approximately', function3(xUser))
# if x is greater than .18
if(xUser > .18):
    print('The stress is approximately', function4(xUser))