# This is a sample Python script.
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 7b(Lab7b_Act2.)
# Date:         10/19/2021
#takes the user input
from collections import Counter

threeString = input('Enter three or more prices separated by spaces: ')
a = []
b = []
a2 =[]
x = 0
y= 0
z = 0

count = Counter(threeString)
for i in range(count[' '] + 1):
    index = threeString.find(' ')
    holder = threeString[:index]
    threeString = threeString[index + 1:]
    if i == count[' ']:
        a.append(threeString)
    else:
        a.append(holder)

for i in range(len(a)):
    a2.append(float(a[i]))

#finds the longest number


strMax = max(a2)
strMaxLen = len(str(strMax))

#adds spaces to the begining of the smallest length numbers
for i in range(len(a)):
    if strMaxLen != len(a[i]):
        holder = ''
        space = strMaxLen - len(a[i])
        for j in range(space):
            holder = ' ' + holder
        b.append(holder+a[i])
    else:
        b.append(a[i])

for j in range(len(a)):
   print('$', str(b[j]))