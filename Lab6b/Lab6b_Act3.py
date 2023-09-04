# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 6b(Lab6b_Act3)
# Date:         10/12/2021
# get user number
strX = input('Enter a four-digit integer: ')
x = int(strX)
xOg = int(strX)
xMin = 0
xMax = 0
strInequality = strX
count = 0
# check if user put a number greater than 10
if len(strX) < 1:
    print('string index out of range')
else:
    for i in range(4 - len(strX)):
        strX = strX + '0'
    x = int(strX)
    # do the calculation
    while(x != 6174 and len(strX)>0 and xOg != 1111 and xOg != 9998):
        xMax1 = max(int(strX[0]), int(strX[1]), int(strX[2]), int(strX[3]))
        i = strX.index(str(xMax1))
        holder1 = strX[i:i + 1]
        xMax1 = strX[0:i] + strX[i + 1:]
        # print(holder1)
        # print(xMax1)

        xMax2 = max(int(xMax1[0]), int(xMax1[1]), int(xMax1[2]))
        i = xMax1.index(str(xMax2))
        holder2 = xMax1[i:i + 1]
        xMax2 = xMax1[:i] + xMax1[i + 1:]
        # print(holder2)
        # print(xMax2)

        xMax3 = max(int(xMax2[0]), int(xMax2[1]))
        i = xMax2.index(str(xMax3))
        holder3 = xMax2[i:i + 1]
        xMax3 = xMax2[:i] + xMax2[i + 1:]
        holder4 = xMax3[0]
        # print(holder3)
        # print(xMax3)
        xMax = holder1 + holder2 + holder3 + holder4
        xMax = int(xMax)

        strMax = str(xMax)
        holder1 = strMax[3]
        holder2 = strMax[2]
        holder3 = strMax[1]
        holder4 = strMax[0]
        xMin = holder1 + holder2 + holder3 + holder4
        xMin = int(xMin)
        x = xMax - xMin
        strX = str(x)
        strInequality = strInequality + ' > ' + strX
        count = count + 1
    #print
    if xOg != 1111:
        print(strInequality)
        print(xOg, 'reaches 6174 via Kaprekar\'s routine in', count, 'iterations')

if xOg == 1111:
    print('1111 > 0')
    print("1111 reaches 0 via Kaprekar's routine in 1 iterations")
