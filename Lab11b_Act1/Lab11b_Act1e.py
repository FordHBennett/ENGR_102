# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act1e
# Date:         11/29/2021

def parte(array):
    array.sort()
    #finds median, max, and min
    if len(array)%2 !=0:
        return (array[0]), (array[(len(array)//2)]),(array[-1])
    else:
        return array[0], ((array[len(array)//2] + (array[len(array)//2 - 1])))/2,(array[-1])