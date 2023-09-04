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

# Define the start and end of the prime calculation
primeStart = 2
primeStop = 100
isPrime = True
totalPrime = 0

# run the for loop from the starting number to the ending number, inclusive
for i in range(primeStart, primeStop + 1):
    # set the prime status to true at the beginning of each loop
    isPrime = True
    # Check all numbers that came before the current number
    for j in range(primeStart, i):
        # If the number is divisible by any of the smaller factors, it isn't prime
        if i % j == 0:
            isPrime = False
    # Print whether the number is prime, and add to the total amount of prime numbers if applicable.
    if isPrime:
        print(i, "is prime")
        totalPrime += 1
    else:
        print(i, "is not prime")

print("There are", totalPrime, "prime numbers between", primeStart, "and", primeStop)
