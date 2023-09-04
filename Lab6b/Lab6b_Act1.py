# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 6b(Lab6b_Act1.)
# Date:         10/12/2021
# get user number
x = int(input('Enter a positive integer to compute the Collatz sequence: '))
print('Here is the Collatz sequence starting at '+str(x)+':')
array1 = []
count = 1
# sumation
while x != 1:
    if x%2 !=0:
        array1.append(x)
        x = (3*x + 1)
        count = count + 1
    else:
        array1.append(x)
        x=int(x/2)
        count = count + 1
if(x == 1):
    array1.append(x)
strArray = str(array1[:])
strArray = strArray[1:-1]
print(strArray)
print('It took',count-1, 'iterations to reach 1')
