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

########### Part A ###########

a = input('Enter True or False for a: ')
b = input('Enter True or False for b: ')
c = input('Enter True or False for c: ')
if a == 'T' or a == 't' or a == 'True':
    a = True
elif a =='F' or a == 'f' or a =='False':
    a = False
else:
    print('error')

if b == 'T' or b == 't' or b == 'True':
    b = True
elif b =='F' or b == 'f' or b =='False':
    b = False
else:
    print('error')
    
if c == 'T' or c == 't' or c == 'True':
    c = True
elif c =='F' or c == 'f' or c =='False':
    c = False
else:
    print('error')
    
########### Part B ###########

print('a and b and c:', a and b and c)
print('a or b or c:', a or b or c)

########### Part C ###########

XOR = not(a and b) and (a or b) and not((not a) and (not b))
print('XOR:', XOR)

odd_number = (a and b and c) or ((not a) and (not b) and c) or ((not b) and (not c) and a) or ((not a) and (not c) and b)
print('Odd number:', odd_number)