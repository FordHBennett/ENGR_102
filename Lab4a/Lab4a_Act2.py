# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Gavin Lane Phillips
#               Ford Hideo Bennett
#               Noah Quinn Hillis
#               Josh Amgad Botros
#               Ian Robert Wiechers
# Section:      472/572
# Assignment:   Lab 4a
# Date:         September 23 2021
#

import math

# Ask user the values they want for the coefficents
a = input("Please enter the coefficient A: ")
b = input("Please enter the coefficient B: ")
c = input("Please enter the coefficient C: ")
# the variables store the absolute values
a2 = str(int(math.fabs(float(a))))
b2 = str(int(math.fabs(float(b))))
c2 = str(int(math.fabs(float(c))))
# Stores values
a3 = int(a)
b3 = int(b)
c3 = int(c)
# used as the index of eqArray
count = 0
# make a variable for the equation
equation = 'The quadratic equation is '
# The array used to store values used later to concatonize a string later
eqArray = ["", a2, "x^2 ", "", b2, "x ", "", c2]


# Function checks to see if a, b, or c holds a value or 1
def whatIsA(array):
    if a2 == "0":
        array[1] = ""
        array[2] = ""
    if a2 == "1":
        array[1] = ""
    if b2 == "0":
        array[4] = ""
        array[5] = ""
    if b2 == "1":
        array[4] = ""
    if c2 == "0":
        array[7] = ""


# Function checks to see if the coeffiecent is neg or pos
def isCoeffiecentNegA():
    if a3 < 0:
        return '- '
    else:
        return ''
def isCoeffiecentNegB():
    if b3 < 0:
        return '- '
    if b3 > 0 and a3 == 0:
        return ''
    if b3 > 0 and a3 != 0:
        return '+ '
    else:
        return ''

def isCoeffiecentNegC():
    if (c3 < 0 and b3 != 0 and a3 !=0) or (c3 < 0 and b3 == 0 and a3 !=0):
        return '- '
    if (c3 > 0 and b3 != 0 and a3 !=0) or (c3 > 0 and b3 == 0 and a3 !=0):
        return '+ '
    if (c3 < 0 and b3 == 0 and a3 ==0) or (c3 < 0 and b3 != 0 and a3 ==0):
        return '- '
    if (c3 > 0 and b3 == 0 and a3 ==0) or (c3 > 0 and b3 != 0 and a3 ==0):
        return '+ '
    else:
        return ''



# calls funcitons
whatIsA(eqArray)
eqArray[0] = isCoeffiecentNegA()
eqArray[3] = isCoeffiecentNegB()
eqArray[6] = isCoeffiecentNegC()
for i in range(8):
    equation = equation + eqArray[count]
    count = count + 1
if(c3 == 0):
    equation = equation[:len(equation)-1]
print(equation, "= 0")




