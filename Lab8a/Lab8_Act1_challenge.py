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

temperature = float(input("Enter a temperature between 0 and 260 deg C: "))
mpa = float(input("Enter a pressure between 5 and 10 MPa: "))
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
mpa10 = [[0, 0.0009952, 0.12, 10.07, 0.0003],
         [20, 0.0009973, 83.31, 93.28, 0.2943],
         [40, 0.0010035, 166.33, 176.37, 0.5685],
         [60, 0.0010127, 249.43, 259.55, 0.826],
         [80, 0.0010244, 332.69, 342.94, 1.0691],
         [100, 0.0010385, 416.23, 426.62, 1.2996],
         [120, 0.0010549, 500.18, 510.73, 1.5191],
         [140, 0.0010738, 584.72, 595.45, 1.7293],
         [160, 0.0010954, 670.06, 681.01, 1.9316],
         [180, 0.0011200, 756.48, 767.68, 2.1271],
         [200, 0.0011482, 844.32, 855.8, 2.3174],
         [220, 0.0011809, 934.01, 945.82, 2.5037],
         [240, 0.0012192, 1026.2, 1038.3, 2.6876],
         [260, 0.0012653, 1121.6, 1134.3, 2.871]]
if temperature < 0 or temperature > 260:
    sys.exit("Temperature is out of range")
if mpa < 5 or mpa > 10:
    sys.exit("Pressure is out of range")


def interpolation(x1, y1, x2, y2, x):
    if x1 == x2:
        y = y1
    else:
        y = ((y2 - y1) / (x2 - x1)) * (x - x1) + y1
    return y


tempMin = math.floor(temperature / 20)
tempMax = math.ceil(temperature / 20)

for i in range(4):
    calculation = interpolation(mpa5[tempMin][0], mpa5[tempMin][i + 1], mpa5[tempMax][0], mpa5[tempMax][i + 1], temperature)
    if i == 0:
        volume1 = calculation
    elif i == 1:
        internalEnergy1 = calculation
    elif i == 2:
        enthalpy1 = calculation
    elif i == 3:
        entropy1 = calculation

for i in range(4):
    calculation = interpolation(mpa10[tempMin][0], mpa10[tempMin][i + 1], mpa10[tempMax][0], mpa10[tempMax][i + 1], temperature)
    if i == 0:
        volume2 = calculation
    elif i == 1:
        internalEnergy2 = calculation
    elif i == 2:
        enthalpy2 = calculation
    elif i == 3:
        entropy2 = calculation

for i in range(4):
    if i == 0:
        volume = interpolation(5, volume1, 10, volume2, mpa)
    elif i == 1:
        internalEnergy = interpolation(5, internalEnergy1, 10, internalEnergy2, mpa)
    elif i == 2:
        enthalpy = interpolation(5, enthalpy1, 10, enthalpy2, mpa)
    elif i == 3:
        entropy = interpolation(5, entropy1, 10, entropy2, mpa)

print("Properties at {:.1f} deg C and {:.1f} MPa are:".format(temperature, mpa))
print("Specific volume (m^3/kg): {:.7f}".format(volume))
print("Specific internal energy (kJ/kg): {:.2f}".format(internalEnergy))
print("Specific enthalpy (kJ/kg): {:.2f}".format(enthalpy))
print("Specific entropy (kJ/kgK): {:.4f}".format(entropy))
