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
# Assignment:   Lab 5a Act 2
# Date:         September 28 2021
#

# User is prompted to input all variables
gender = input("Enter your sex (M/F): ")
age = int(input("Enter your age (years): "))
cigarettes = input("Do you smoke cigarettes (Y/N)? ")
cholesterol = int(input("Enter your total cholesterol (mg/dL): "))
hDLCholesterol = int(input("Enter your HDL cholesterol (mg/dL): "))
bp = int(input("Enter your systolic BP (mmHg): "))
medication = input("Are you taking blood pressure medication (Y/N)? ")
pointTotal = 0

# User's gender, whether they smoke, and if they take medication are converted to booleans
if gender == "M" or gender == "m":
    isMale = True
else:
    isMale = False

if cigarettes == "Y" or cigarettes == "y":
    doesSmoke = True
else:
    doesSmoke = False

if medication == "Y" or medication == "y":
    takesMedication = True
else:
    takesMedication = False

# Changes calculation whether user is male or female
if isMale:
    # Adds or takes away from point total based on age
    if 20 <= age <= 34:
        pointTotal -= 9
    elif 35 <= age <= 39:
        pointTotal -= 4
    elif 45 <= age <= 49:
        pointTotal += 3
    elif 50 <= age <= 54:
        pointTotal += 6
    elif 55 <= age <= 59:
        pointTotal += 8
    elif 60 <= age <= 64:
        pointTotal += 10
    elif 65 <= age <= 69:
        pointTotal += 11
    elif 70 <= age <= 74:
        pointTotal += 12
    elif 75 <= age <= 79:
        pointTotal += 13

    # Adds or takes away from point total based on age and total cholesterol
    if 160 <= cholesterol <= 199 and 20 <= age <= 39:
        pointTotal += 4
    elif 160 <= cholesterol <= 199 and 40 <= age <= 49:
        pointTotal += 3
    elif 160 <= cholesterol <= 199 and 50 <= age <= 59:
        pointTotal += 2
    elif 160 <= cholesterol <= 199 and 60 <= age <= 69:
        pointTotal += 1
    elif 200 <= cholesterol <= 239 and 20 <= age <= 39:
        pointTotal += 7
    elif 200 <= cholesterol <= 239 and 40 <= age <= 49:
        pointTotal += 5
    elif 200 <= cholesterol <= 239 and 50 <= age <= 59:
        pointTotal += 3
    elif 200 <= cholesterol <= 239 and 60 <= age <= 69:
        pointTotal += 1
    elif 240 <= cholesterol <= 279 and 20 <= age <= 39:
        pointTotal += 9
    elif 240 <= cholesterol <= 279 and 40 <= age <= 49:
        pointTotal += 6
    elif 240 <= cholesterol <= 279 and 50 <= age <= 59:
        pointTotal += 4
    elif 240 <= cholesterol <= 279 and 60 <= age <= 69:
        pointTotal += 2
    elif 240 <= cholesterol <= 279 and 70 <= age <= 79:
        pointTotal += 1
    elif 280 <= cholesterol and 20 <= age <= 39:
        pointTotal += 11
    elif 280 <= cholesterol and 40 <= age <= 49:
        pointTotal += 8
    elif 280 <= cholesterol and 50 <= age <= 59:
        pointTotal += 5
    elif 280 <= cholesterol and 60 <= age <= 69:
        pointTotal += 3
    elif 280 <= cholesterol and 70 <= age <= 79:
        pointTotal += 1

    # Adds or takes away from point total based on age and whether or not the user is a smoker
    if doesSmoke and 20 <= age <= 39:
        pointTotal += 8
    elif doesSmoke and 40 <= age <= 49:
        pointTotal += 5
    elif doesSmoke and 50 <= age <= 59:
        pointTotal += 3
    elif doesSmoke and 60 <= age <= 79:
        pointTotal += 1

    # Adds or takes away from point total based on HDL cholesterol
    if hDLCholesterol >= 60:
        pointTotal -= 1
    elif 40 <= hDLCholesterol <= 49:
        pointTotal += 1
    elif 40 > hDLCholesterol:
        pointTotal += 2

    # Adds or takes away from point total based on systolic bp and whether or not the user is taking medicine
    if takesMedication and 120 <= bp <= 129:
        pointTotal += 1
    elif takesMedication and 130 <= bp <= 159:
        pointTotal += 2
    elif takesMedication and 160 <= bp:
        pointTotal += 3
    elif 130 <= bp <= 159:
        pointTotal += 1
    elif 160 <= bp:
        pointTotal += 2

    # Calculates risk of heart attack based on point total
    if pointTotal < 0:
        percentage = "<1"
    elif 0 <= pointTotal <= 4:
        percentage = "1"
    elif 5 <= pointTotal <= 6:
        percentage = "2"
    elif 7 == pointTotal:
        percentage = "3"
    elif 8 == pointTotal:
        percentage = "4"
    elif 9 == pointTotal:
        percentage = "5"
    elif 10 == pointTotal:
        percentage = "6"
    elif 11 == pointTotal:
        percentage = "8"
    elif 12 == pointTotal:
        percentage = "10"
    elif 13 == pointTotal:
        percentage = "12"
    elif 14 == pointTotal:
        percentage = "16"
    elif 15 == pointTotal:
        percentage = "20"
    elif 16 == pointTotal:
        percentage = "25"
    elif 17 <= pointTotal:
        percentage = ">30"
else:
    # Adds or takes away from point total based on age
    if 20 <= age <= 34:
        pointTotal -= 7
    elif 35 <= age <= 39:
        pointTotal -= 3
    elif 45 <= age <= 49:
        pointTotal += 3
    elif 50 <= age <= 54:
        pointTotal += 6
    elif 55 <= age <= 59:
        pointTotal += 8
    elif 60 <= age <= 64:
        pointTotal += 10
    elif 65 <= age <= 69:
        pointTotal += 12
    elif 70 <= age <= 74:
        pointTotal += 14
    elif 75 <= age <= 79:
        pointTotal += 16

    # Adds or takes away from point total based on age and total cholesterol
    if 160 <= cholesterol <= 199 and 20 <= age <= 39:
        pointTotal += 4
    elif 160 <= cholesterol <= 199 and 40 <= age <= 49:
        pointTotal += 3
    elif 160 <= cholesterol <= 199 and 50 <= age <= 59:
        pointTotal += 2
    elif 160 <= cholesterol <= 199 and 60 <= age <= 69:
        pointTotal += 1
    elif 160 <= cholesterol <= 199 and 70 <= age <= 79:
        pointTotal += 1
    elif 200 <= cholesterol <= 239 and 20 <= age <= 39:
        pointTotal += 8
    elif 200 <= cholesterol <= 239 and 40 <= age <= 49:
        pointTotal += 6
    elif 200 <= cholesterol <= 239 and 50 <= age <= 59:
        pointTotal += 4
    elif 200 <= cholesterol <= 239 and 60 <= age <= 69:
        pointTotal += 2
    elif 200 <= cholesterol <= 239 and 70 <= age <= 79:
        pointTotal += 1
    elif 240 <= cholesterol <= 279 and 20 <= age <= 39:
        pointTotal += 11
    elif 240 <= cholesterol <= 279 and 40 <= age <= 49:
        pointTotal += 8
    elif 240 <= cholesterol <= 279 and 50 <= age <= 59:
        pointTotal += 5
    elif 240 <= cholesterol <= 279 and 60 <= age <= 69:
        pointTotal += 3
    elif 240 <= cholesterol <= 279 and 70 <= age <= 79:
        pointTotal += 2
    elif 280 <= cholesterol and 20 <= age <= 39:
        pointTotal += 13
    elif 280 <= cholesterol and 40 <= age <= 49:
        pointTotal += 10
    elif 280 <= cholesterol and 50 <= age <= 59:
        pointTotal += 7
    elif 280 <= cholesterol and 60 <= age <= 69:
        pointTotal += 4
    elif 280 <= cholesterol and 70 <= age <= 79:
        pointTotal += 2

    # Adds or takes away from point total based on age and whether or not the user is a smoker
    if doesSmoke and 20 <= age <= 39:
        pointTotal += 9
    elif doesSmoke and 40 <= age <= 49:
        pointTotal += 7
    elif doesSmoke and 50 <= age <= 59:
        pointTotal += 4
    elif doesSmoke and 60 <= age <= 69:
        pointTotal += 2
    elif doesSmoke and 70 <= age <= 79:
        pointTotal += 1

    # Adds or takes away from point total based on HDL cholesterol
    if hDLCholesterol >= 60:
        pointTotal -= 1
    elif 40 <= hDLCholesterol <= 49:
        pointTotal += 1
    elif 40 > hDLCholesterol:
        pointTotal += 2

    # Adds or takes away from point total based on systolic bp and whether or not the user is taking medicine
    if takesMedication and 120 <= bp <= 129:
        pointTotal += 3
    elif takesMedication and 130 <= bp <= 139:
        pointTotal += 4
    elif takesMedication and 140 <= bp <= 159:
        pointTotal += 5
    elif takesMedication and 160 <= bp:
        pointTotal += 6
    elif 120 <= bp <= 129:
        pointTotal += 1
    elif 130 <= bp <= 139:
        pointTotal += 2
    elif 140 <= bp <= 159:
        pointTotal += 3
    elif 160 <= bp:
        pointTotal += 4

    # Calculates risk of heart attack based on point total
    if pointTotal < 9:
        percentage = "<1"
    elif 9 <= pointTotal <= 12:
        percentage = "1"
    elif 13 <= pointTotal <= 14:
        percentage = "2"
    elif 15 == pointTotal:
        percentage = "3"
    elif 16 == pointTotal:
        percentage = "4"
    elif 17 == pointTotal:
        percentage = "5"
    elif 18 == pointTotal:
        percentage = "6"
    elif 19 == pointTotal:
        percentage = "8"
    elif 20 == pointTotal:
        percentage = "11"
    elif 21 == pointTotal:
        percentage = "14"
    elif 22 == pointTotal:
        percentage = "17"
    elif 23 == pointTotal:
        percentage = "22"
    elif 24 == pointTotal:
        percentage = "27"
    elif 25 <= pointTotal:
        percentage = ">30"

print("Your 10-year risk of a heart attack is ", percentage, "%", sep="")
