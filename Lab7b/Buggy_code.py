# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Gavin Lane Phillips
#               Ford Hideo Bennett
#               Noah Quinn Hillis
#               Josh Amgad Botros
#               Ian Robert Wiechers
# Section:      472/572
# Assignment:   Buggy code
# Date:         10/26/21
#

# Correct output:
# The median is 67.5
# The mean is 68.52
# The standard deviation is 16.98144870145065
from math import sqrt
# grade data list
gradeData = [79,99,73,49,67,62,52,99,57,58,67,88,71,69,41,74,53,90,63,66,92,54,61,59,48,71,83,89,99,69,66,40,48,41,99,68,52,78,77,71,40,65,77,87,96,44,54,60,89,72]
# Part A
# Fake Sort algorithm: add min to new list, remove from old
# make a copy of gradeData so it's not overwritten
oldlist = gradeData[:]
newlist = []
for i in range(len(oldlist)):
   newlist.append(min(oldlist))
   oldlist.remove(min(oldlist))
# Part B
# find median value, no need for loops
if len(newlist) % 2 == 0:
   # even number of elements
   a = (len(newlist) // 2) - 1
   b = a + 1
   median = (newlist[a] + newlist[b]) / 2
else:
   # odd number of elements
   median = newlist[(len(newlist) - 1) // 2]
# Part C
# find mean and standard deviation
# use population stdev equation: σ = sqrt((Σ(x - mean)^2)/n)
xbar = sum(newlist) / len(newlist)
stdev = 0
for x in range(len(newlist)):
   stdev = ((newlist[x] - xbar) ** 2) + stdev
   if x == len(newlist)-1:
      stdev = sqrt(stdev / len(newlist))
# print results
print("The median is", median)
print("The mean is", xbar)
print("The standard deviation is", stdev)
