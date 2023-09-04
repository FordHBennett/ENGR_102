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

# Open the 2 passport files
passportFiles = open("Lab9a_input.txt", 'r')
newPassportFile = open("Lab9a_Act1a_valid.txt", 'w')

# Include stored variables
currentPassport = dict()
rawText = ""
validPassports = 0


# Check if passport is valid
def CheckValidity(passport):
	valid = False
	if "byr" in passport:
		if "iyr" in passport:
			if "eyr" in passport:
				if "hgt" in passport:
					if "hcl" in passport:
						if "ecl" in passport:
							if "pid" in passport:
								valid = True

	return valid


for next_line in passportFiles:
	currentLine = next_line.split(' ')
	count = 0
	for thisVariable in currentLine:
		currentLine[count] = thisVariable.split(':')
		count += 1
	if next_line == '\n':
		isValid = CheckValidity(currentPassport)
		if isValid:
			newPassportFile.write(rawText + '\n')
			validPassports += 1
		currentPassport = dict()
		rawText = ""
	else:
		if rawText == "":
			rawText += next_line
		else:
			rawText += next_line
		for variable in currentLine:
			currentPassport[variable[0]] = variable[1]

passportFiles.close()
newPassportFile.close()
print("There are", validPassports, "valid passports")
