# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Ian Wiechers
#               Josh Botros
#               Ford Bennett
#               Gavin Phillips
#               Noah Hillis
# Section:      572
# Assignment:   Lab 2a Act 3
# Date:         9   9   2021

import math
t1 = 10
t2 = 55
y1 = 2025
y2 = 23025
endpoint1 = 0
endpoint2 = 0
r = 6745

endpoint1 = (y2 - y1)/(t2 - t1)
endpoint1 = endpoint1*(25-t1)
endpoint1 = endpoint1 + y1
print("Part 1:")
print("For t = 25 minutes, the position p =", endpoint1, "kilometers")

c = 2*math.pi*r
endpoint2 = (y2 - y1)/(t2 - t1)
endpoint2 = endpoint2*(300-t1)
endpoint2 = endpoint2 + y1
endpoint2 = endpoint2%c
print("Part 2:")
print("For t = 5 hours, the position p =", endpoint2, "kilometers")

