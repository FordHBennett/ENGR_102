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
# Assignment:   Lab 6a
# Date:         10/5/2021
#

import math
import sys

# This is where the user enters in the temperature
temperature = float(input("Enter a temperature between 0 and 260 deg C: "))
# Define the MPA 5 Table as a list of lists
mpa5 = [[0, 0.0009977, 0.04, 5.03, 0.0001],
        [20, 0.0009996, 83.61, 88.61, 0.2954],
        [40, 0.0010057, 166.92, 171.95, 0.5705],
        [60, 0.0010149, 250.29, 255.36, 0.8287],
        [80, 0.0010267, 333.82, 338.96, 1.0723],
        [100, 0.0010410, 417.65, 422.85, 1.3034],
        [120, 0.0010576, 501.91, 507.19, 1.5236],
        [140, 0.0010769, 586.8, 592.18, 1.7344],
        [160, 0.0010988, 672.55, 678.04, 1.9374],
        [180, 0.0011240, 759.47, 765.09, 2.1338],
        [200, 0.0011531, 847.92, 853.68, 2.3251],
        [220, 0.0011868, 938.39, 944.32, 2.5127],
        [240, 0.0012268, 1031.6, 1037.7, 2.6983],
        [260, 0.0012755, 1128.5, 1134.9, 2.8841]]
# Check if the temperature is less than 0 or greater than 260. If so show error
if temperature < 0 or temperature > 260:
    sys.exit("Temperature is out of range")


# Make Interpolation function. Enter in the first x and y values, second x and y values, and the desired x value
def interpolation(x1, y1, x2, y2, x):
    # Check to see if both positions are the same, so as not to divide by zero
    if x1 == x2:
        # If both positions are the same, the y values will also be the same
        y = y1
    else:
        # Use the interpolation function to create y
        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
    # Return y
    return y


# Get the temperatures that bracket the user input temperature
# Put these temperatures at the values that would identify the on the list
tempMin = math.floor(temperature / 20)
tempMax = math.ceil(temperature / 20)

# Run a loop 4 times to get all 4 variables
for i in range(4):
    # Run the interpolation with the the bracketed temperatures, their associated variable, and the temperature
    calculation = interpolation(mpa5[tempMin][0], mpa5[tempMin][i + 1], mpa5[tempMax][0], mpa5[tempMax][i + 1], temperature)
    # Run an if statement to assign the calcualted variable to the desired variable
    if i == 0:
        volume = calculation
    elif i == 1:
        internalEnergy = calculation
    elif i == 2:
        enthalpy = calculation
    elif i == 3:
        entropy = calculation

# Print that shiz
print("Properties at {:.1f} deg C are:".format(temperature))
print("Specific volume (m^3/kg): {:.7f}".format(volume))
print("Specific internal energy (kJ/kg): {:.2f}".format(internalEnergy))
print("Specific enthalpy (kJ/kg): {:.2f}".format(enthalpy))
print("Specific entropy (kJ/kgK): {:.4f}".format(entropy))
