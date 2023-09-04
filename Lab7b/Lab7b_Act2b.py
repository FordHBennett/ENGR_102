# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 6b(Lab6b_Act1.)
# Date:         10/12/2021
#takes the user input
from collections import Counter
from itertools import count

values = input('Enter three or more values separated by spaces: ')
sep = input('Enter a two-character separator: ')
a = []
aStr = ''
count = Counter(values)
#finds the number by finding the first space and splicing the the string from the begining to the space
for i in range(count[' '] + 1):
    index = values.find(' ')
    holder = values[:index]
    values = values[index + 1:]
    if i == count[' ']:
        a.append(values)
    else:
        a.append(holder)

for i in range(len(a)):
        aStr = aStr+ ' ' + sep + ' ' +a[i]
#splices the string
aStr = aStr[4:]
#prints the numbers with -> seperating each number
print(aStr)