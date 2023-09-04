# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act1b
# Date:         11/29/2021

def partb(a,b,c):
    #creat lists
    total = []
    holder =[]
    #find the profitability
    for i in range(len(a)):
        total.append(b[i]-c[i])
    for i in range(len(total)):
        holder.append(total[i])
    #find the index of the most profitable
    holder.sort()
    best = holder[0]
    index = total.index(best)
    return a[index], abs(best)