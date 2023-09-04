# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act1f
# Date:         11/29/2021

def partf(a,b):
    velo = []
    #finds slope
    for i in range(len(a)-1):
        velo.append((b[i+1]-b[i])/(a[i+1]-a[i]))
    return velo

