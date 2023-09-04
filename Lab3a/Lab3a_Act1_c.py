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

atmospheres = float(input("Please enter the number of atmospheres to be converted to millimeters of mercury: "))
# asks to enter the number of atmospheres

mmHg = atmospheres * 760
# converts atmospheres to millimeters of mercury

print("{:.2f} atmospheres is equivalent to {:.2f} millimeters of mercury" .format(atmospheres, mmHg))
# prints conversion
