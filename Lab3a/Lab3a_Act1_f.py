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
# Assignment:   Lab 3a Act 1
# Date:         September 14 2021
#

celsius = float(input("Please enter the number of degrees Celsius to be converted to degrees Rankine: "))
# asks to enter the degrees celsius

rankine = (celsius + 273.15) * (9/5)
# converts degrees celsius to degrees rankine

print("{:.2f} degrees Celsius is equivalent to {:.2f} degrees Rankine" .format(celsius, rankine))
# prints conversion
