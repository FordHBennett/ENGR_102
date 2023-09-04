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
newPassportFile = open("Lab9a_Act1b_valid.txt", 'w')

# Include stored variables
currentPassport = dict()
rawText = ""
validPassports = 0


# Check if passport is valid
def CheckValidity(passport):
	valid = 0
	hairValid = 0
	if "byr" in passport:
		if 1920 <= int(passport["byr"]) <= 2005:
			valid += 1
	if "iyr" in passport:
		if 2011 <= int(passport["iyr"]) <= 2021:
			valid += 1
	if "eyr" in passport:
		if 2021 <= int(passport["eyr"]) <= 2031:
			valid += 1
	if "hgt" in passport:
		if passport["hgt"][3:5] == "cm":
			if 150 <= int(passport["hgt"][0:3]) <= 193:
				valid += 1
		elif passport["hgt"][2:4] == "in":
			if 59 <= int(passport["hgt"][0:2]) <= 76:
				valid += 1
	if "hcl" in passport:
		if passport["hcl"][0] == "#":
			for i in passport["hcl"]:
				if i != "#":
					if i in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"):
						hairValid += 1
			if hairValid == 6:
				valid += 1
	if "ecl" in passport:
		if passport["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
			valid += 1
	if "pid" in passport:
		if len(passport["pid"]) == 9:
			valid += 1

	if valid == 7:
		valid = True
	else:
		valid = False
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
