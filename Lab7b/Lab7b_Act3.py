# This is a sample Python script.
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 7b(Lab7b_Act2.)
# Date:         10/19/2021
import math
#gets user numbers
from collections import Counter

aStr = input('Enter the elements for vector A: ')
bStr = input('Enter the elements for vector B: ')
#creates empty arrays and varibles
a = []
b = []
aMag = 0
bMag = 0
aPlusB = []
aMinusB = []
dotProduct = 0

count = Counter(aStr)
for i in range(count[' '] + 1):
    index = aStr.find(' ')
    holder = aStr[:index]
    aStr = aStr[index + 1:]
    if i == count[' ']:
        a.append(float(aStr))
    else:
        a.append(float(holder))

for i in range(count[' '] + 1):
    index = bStr.find(' ')
    holder = bStr[:index]
    bStr = bStr[index + 1:]
    if i == count[' ']:
        b.append(float(bStr))
    else:
        b.append(float(holder))


#calculates the magnitude of each vetor
for i in range(len(a)):
    aMag = a[i]**2 + aMag
aMag = math.sqrt(aMag)
for i in range(len(a)):
    bMag = b[i]**2 + bMag
bMag = math.sqrt(bMag)

# does dot addition and subtraction
for i in range(len(a)):
    t = a[i] + b[i]
    aPlusB.append(t)
for i in range(len(a)):
    t = a[i] - b[i]
    aMinusB.append(t)
#calc dotProduct
for i in range(len(a)):
    dotProduct = a[i] * b[i] + dotProduct

#prints
print('The magnitude of vector A is '+ '{:.4f}'.format(aMag))
print('The magnitude of vector B is '+'{:.4f}'.format(bMag))
print('A + B is', aPlusB)
print('A - B is', aMinusB)
print('The dot product is', dotProduct)
