# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Ian Wiechers
#               Josh Botros
#               Ford Bennett
#               Gavin Phillips
#               Noah Hillis
# Section:      572
# Assignment:   Lab 3a Act 2
# Date:         9   14   2021

import math

t1 = float(input('Enter time 1: '))
x1 = float(input('Enter the x position of the object at time 1: '))
y1 = float(input('Enter the y position of the object at time 1: '))
z1 = float(input('Enter the z position of the object at time 1: '))
t2 = float(input('Enter time 2: '))
x2 = float(input('Enter the x position of the object at time 2: '))
y2 = float(input('Enter the y position of the object at time 2: '))
z2 = float(input('Enter the z position of the object at time 2: '))
x0 = 0
y0 = 0
z0 = 0
#This calculates the increments of time
iFifth = (t2 - t1) / 4
counter = t1
printCounter = 0

#This interpolates the x value
def interpolate(time):
    x0 = (x2 - x1) / (t2 - t1)
    x0 = x0 * (time - t1)
    x0 = x0 + x1
    return x0

#This interpolates the y value
def setValuesY(time):
    y0 = (y2 - y1) / (t2 - t1)
    y0 = y0 * (time - t1)
    y0 = y0 + y1
    return y0

#This interpolates the y value
def setValuesZ(time):
    z0 = (z2 - z1) / (t2 - t1)
    z0 = z0 * (time - t1)
    z0 = z0 + z1
    return z0

#This for loop prints out the x, y and z value rounded to the nearest .00
for i in range(5):
    #If it is the first time going through the loop then add a /n if not don't
    if printCounter <= 0:
        print('\nAt time {:.1f} seconds the object is at'.format(counter), '({:.2f},'.format(interpolate(counter)),
              '{:.2f},'.format(setValuesY(counter)), '{:.2f})'.format(setValuesZ(counter)))
        printCounter = printCounter + 1
        counter = counter + iFifth
    else:
        print('At time {:.1f} seconds the object is at'.format(counter), '({:.2f},'.format(interpolate(counter)),
              '{:.2f},'.format(setValuesY(counter)), '{:.2f})'.format(setValuesZ(counter)))
        counter = counter + iFifth
