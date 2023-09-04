# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:       Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 4b Act 4
# Date:         September 30 2021
import numpy
import numpy as np
import sympy
from sympy import var, solve

a = int(input('Please enter the coefficient A: '))
b = int(input('Please enter the coefficient B: '))
c = int(input('Please enter the coefficient C: '))
x = var('x')
roots = solve(a * (x ** 2) + b * x + c,x)
arrayRoot1 = []
arrayRoot2 = []

def convertStr():
    count1 = 0
    count2 = 0
    root1 = roots[0]
    root2 = roots[1]
    for i in range(len(root1)):
        arrayRoot1[count1] = root1[count1]
        count1 = count1 + 1
    for i in range(len(root2)):
        arrayRoot2[count2] = root2[count2]
        count2 = count2 + 1


#if np.iscomplex(roots[0] == True):
    #convertStr()
    #print(arrayRoot1,arrayRoot2)
    #print(roots)

if(len(roots) == 1):
    print('The root is x =', float(roots[0]))
elif(a!=0 or b!=0) :
    print('The roots are x =', float(roots[1]), 'and x =', float(roots[0]))
if(a == 0 and b == 0):
    print('You entered an invalid combination of coefficients')


