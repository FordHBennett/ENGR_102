# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:   Ford Hideo Bennett

# Section:      472/572
# Assignment:   Lab 4b act 1
# Date:         September 28 2021
a= int(input('Please enter a positive value for day: '))
aPastTen = 0
aw = 0
# Checks if the day is invalid
if (a < 0):
    print('You entered an invalid number!')
# it is the for loop but extended
if 0 <= a:
    if(a<10):
        aw = a * 10
    if(a>9):
        aw = 100
        if a>= 11:
            aPastTen= aPastTen+ 11
            if a>= 12:
                aPastTen= aPastTen+ 12
                if ( a>= 13):
                    aPastTen= aPastTen+ 13
                    if (a>= 14):
                        aPastTen= aPastTen+ 14
                        if (a>= 15):
                            aPastTen= aPastTen+ 15
                            if (a>= 16):
                                aPastTen= aPastTen+ 16
                                if (a>= 17):
                                    aPastTen= aPastTen+ 17
                                    if (a>= 18):
                                        aPastTen= aPastTen+ 18
                                        if (a>= 19):
                                            aPastTen= aPastTen+ 19
                                            if (a>= 20):
                                                aPastTen= aPastTen+ 20
                                                if (a>= 21):
                                                    aPastTen= aPastTen+ 21
                                                    if (a>= 22):
                                                        aPastTen= aPastTen+ 22
                                                        if (a>= 23):
                                                            aPastTen= aPastTen+ 23
                                                            if (a>= 24):
                                                                aPastTen= aPastTen+ 24
                                                                if (a>= 25):
                                                                    aPastTen= aPastTen+ 25
                                                                    if (a>= 26):
                                                                        aPastTen= aPastTen+ 26
                                                                        if (a>= 27):
                                                                            aPastTen= aPastTen+ 27
                                                                            if (a>= 28):
                                                                                aPastTen= aPastTen+ 28
                                                                                if (a>= 29):
                                                                                    aPastTen= aPastTen+ 29
                                                                                    if (a>= 30):
                                                                                        aPastTen= aPastTen+ 30
                                                                                        if (a>= 31):
                                                                                            aPastTen= aPastTen+ 31
                                                                                            if (a>= 32):
                                                                                                aPastTen= aPastTen+ 32
                                                                                                if (a>= 33):
                                                                                                    aPastTen= aPastTen+ 33
                                                                                                    if (a>= 34):
                                                                                                        aPastTen= aPastTen+ 34
                                                                                                        if (a>= 35):
                                                                                                            aPastTen= aPastTen+ 35
                                                                                                            if (a>= 36):
                                                                                                                aPastTen= aPastTen+ 36
                                                                                                                if (a>= 37):
                                                                                                                    aPastTen= aPastTen+ 37
                                                                                                                    if ( a>= 38):
                                                                                                                        aPastTen= aPastTen+ 38
                                                                                                                        if (a>= 39):
                                                                                                                            aPastTen= aPastTen+ 39
                                                                                                                            if (a>= 40):
                                                                                                                                aPastTen= aPastTen+ 40
                                                                                                                                if (a>= 41):
                                                                                                                                    aPastTen= aPastTen+ 41
                                                                                                                                    if (a>= 42):
                                                                                                                                        aPastTen= aPastTen+ 42
                                                                                                                                        if (a>= 43):
                                                                                                                                            aPastTen= aPastTen+ 43
                                                                                                                                            if (a>= 44):
                                                                                                                                                aPastTen= aPastTen+ 44
                                                                                                                                                if (a>= 45):
                                                                                                                                                    aPastTen= aPastTen+ 45
                                                                                                                                                    if (a>= 46):
                                                                                                                                                        aPastTen= aPastTen+ 46
                                                                                                                                                        if ( a>= 47):
                                                                                                                                                            aPastTen= aPastTen+ 47
                                                                                                                                                            if ( a>= 48):
                                                                                                                                                                aPastTen= aPastTen+ 48
                                                                                                                                                                if (a>= 49):
                                                                                                                                                                    aPastTen= aPastTen+ 49
                                                                                                                                                                    if (a>= 50):
                                                                                                                                                                        aPastTen= aPastTen+ 50
                                                                                                                                                                        if (a > 50):
                                                                                                                                                                            aPastTen = aPastTen + ((a - 50) * 50)
                                                                                                                                                                            if(a>100):
                                                                                                                                                                                aPastTen = aPastTen - ((a - 100)*50)

if 0 <= a:
    print('The total number of widgets produced on day', a, 'is', aw+aPastTen)