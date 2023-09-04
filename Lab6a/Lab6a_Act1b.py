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

sideLength = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

# Start by adding the sides of pyramid
sides = (layers * (2 * 4 + (layers - 1) * 4)) / 2
# Add the visible top sides of the pyramid
sides += ((layers - 1) * (2 * 3 + ((layers - 1) - 1) * 2)) / 2
# Add one for the remaining very top of the pyramid
sides += 1

# make the total area the sides multiplied by the area
totalArea = sides * (sideLength ** 2)

print("You need {:.2f} square meters of gold foil to cover the pyramid" .format(totalArea))
