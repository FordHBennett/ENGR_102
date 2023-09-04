# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 6b(Lab6b_Act2)
# Date:         10/12/2021
x = int(input('Enter an integer: '))
countSum = 0
count =0
# sums the numbers between 0 and the users number
for i in range(x+1):
    countSum = countSum + count
    count = count + 1
print('The sum of all integers from', 0, 'to', x, 'is', countSum)
count = 1
countProduct = 1
# multiplies the numbers between 1 and the user number
for i in range(x):
    countProduct = countProduct * count
    count = count + 1
print('The product of all integers from', 1, 'to', x, 'is', countProduct)