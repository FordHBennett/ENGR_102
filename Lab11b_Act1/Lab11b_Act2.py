# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ford Hideo Bennett
# Section:      472/572
# Assignment:   Lab 11b_Act2
# Date:         11/29/2021
from random import randint

randomNumber = randint(1, 100)

import random

again = 0


# gets the users initail number and call guess function
def ask():
    global again
    again = again + 1
    number = int(input('Guess the secret number! Hint: it’s an integer between 1 and 100:'))
    guess(number)


# gets the random number
def ranNum():
    return randint(1, 10)


randomNum = ranNum()


def guess(num):
    global again
    global randomNum
    correct = True
    # checks if random number is equal to user number
    while correct:
        if num > randomNum:
            print('Too high!')
            again = again + 1
        elif num < randomNum:
            print('Too low!')
            again = again + 1
        elif num == randomNum:
            break
        num = int(input("What number do you guess? "))
    if num == randomNum:
        print('You guessed it!', 'It took you', again, 'guesses.')


ask()
