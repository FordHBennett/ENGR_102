# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Act2.)
# Date:         21/9/2021
from math import *
area = float(input('Please enter the area: '))
# calc raduis or side length and print
def raduisCircle(a):
    r = sqrt(a/pi)
    print('A circle with area {:.2f} has a radius {:.3f}'.format(a, r))
def lengthEqualTriange(a):
    s = sqrt((a*4)/sqrt(3))
    print('An equilateral triangle with area {:.2f} has a side {:.3f}'.format(a, s))
def lengthSquare(a):
    s = sqrt(a)
    print('A square with area {:.2f} has a side {:.3f}'.format(a, s))
def lengthPentagon(a):
    s = sqrt(((4*a*tan(pi/5))/5))
    print('A pentagon with area {:.2f} has a side {:.3f}'.format(a, s))
def lengthDecagon(a):
    s = sqrt(((4*a*tan(pi/12))/12))
    print('A dodecagon with area {:.2f} has a side'.format(a), round(s,3))
#call funcitons
raduisCircle(area)
lengthEqualTriange(area)
lengthSquare(area)
lengthPentagon(area)
lengthDecagon(area)