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
# Assignment:   ASSIGNMENT HERE
# Date:         DATE HERE
#

import math

# Enter in the number of hours

print("Enter the hours parked as a decimal number. Include a negative sign if the ticket is lost.")
time = float(input("Please enter the hours parked: "))

# Calculate the cost based on whole days and create tempTime for remaining hours

cost = math.ceil(math.fabs(time)) // 24 * 24
tempTime = math.ceil(math.fabs(time)) % 24

# Use the remaining hours to calculate the additional cost on top of days
if 0 < tempTime <= 2:
    tempCost = 4
elif 2 < tempTime <= 4:
    tempCost = 7
elif 4 < tempTime <= 20:
    tempCost = 7 + (tempTime - 4)
elif 20 < tempTime <= 24:
    tempCost = 24
else:
    tempCost = 0

# Add the 2 cost variables together and add lost ticket fee if possible
cost += tempCost
if time < 0:
    cost += 36

print("Parking for ", time, " hours please pay $", cost, sep='')
