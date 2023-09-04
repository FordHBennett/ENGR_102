# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Name:         Ford Bennett
# Section:      572
# Assignment:   Lab 7b(Lab7b_Act1.)
# Date:         10/19/2021

name = input('What is your name? ')
lowerCaseName = name.lower()
letter = []
#Finds the index of the first vowel
for i in range(len(name)):
    if(lowerCaseName[i] == 'a' or  lowerCaseName[i] == 'e' or lowerCaseName[i] == 'i' or lowerCaseName[i] == 'o' or lowerCaseName[i] == 'u'):
        letter.append(i)
if(name[0]== 'a' or name[0]== 'e' or name[0]== 'i' or name[0]== 'o' or name[0]== 'u'):
    letter[0] = letter[0].lowercase

#splices the string
y = lowerCaseName[letter[0]:]
print(name + ',', name+ ',', 'Bo-B'+y)
print('Banana-Fana Fo-F'+y)
print('Me Mi Mo-M'+y)
print(name+'!')