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
totalArea = 0

for i in range(1, layers + 1):
    # Start by adding the top sides of the pyramid
    totalArea += sideLength ** 2 * i ** 2
    # Add the sides of the pyramid
    totalArea += sideLength ** 2 * i * 4
    # subtract the top sides covered by other squares
    totalArea -= sideLength ** 2 * (i - 1) ** 2

print("You need {:.2f} square meters of gold foil to cover the pyramid" .format(totalArea))
