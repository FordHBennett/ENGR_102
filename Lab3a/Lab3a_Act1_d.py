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

watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))
# asks to enter the number of watts

btu = watts * 3.412141633
# converts watts to BTU per hour

print("{:.2f} watts is equivalent to {:.2f} BTU per hour" .format(watts, btu))
# prints conversion
