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

lps = float(input("Please enter the number of liters per second to be converted to gallons per minute: "))
# asks to enter the number of liters per second

gpm = lps * 15.850323141489
# converts liters per second to gallons per minute

print("{:.2f} liters per second is equivalent to {:.2f} gallons per minute" .format(lps, gpm))
# prints conversion
