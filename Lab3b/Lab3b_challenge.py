# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 3b(Lab3b_Challenge.)
# Date:         21/9/2021
import math
from math import*
a = int(input('Please enter the number of digits of precision for pi: ')) + 1
listDigits = []
roundedPi = ''
digit = ''
def arrayPi():
    arrayCount = 0
    piStr = str(math.pi)
    for i in range(15):
        digit = piStr[arrayCount]
        listDigits.append(digit)
        arrayCount = arrayCount + 1

def roundPi(input):
    global roundedPi
    input = input +1
    arrayCount1 = 0
    arrayCount2 = 0
    for i in range(input):
        listDigits.append(listDigits[arrayCount1])
        arrayCount1 = arrayCount1 + 1
    for i in range(input):
        roundedPi = roundedPi + listDigits[arrayCount2]
        arrayCount2 = arrayCount2 + 1


arrayPi()
roundPi(a)
print('The value of pi to', a-1, 'digits is:', roundedPi)