# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:   Ford Hideo Bennett

# Section:      472/572
# Assignment:   Lab 4b act 1
# Date:         September 28 2021
#
from math import sqrt
a = 1/7
print('a =', a)
b = a * 7
print('b = a * 7 =', b)
# Part A: No b should be a float becuase a is a float and a float * an int = float

c = 2 * a
d = 5 * a
f = c + d
print('f = 2 * a + 5 * a =', f)
# Part A: No because you are multipying by a float

x = sqrt(1 / 3)
print('x =', x)
y = x * x * 3
print('y = x * x * 3 =', y)
z = x * 3 * x
print('z = x * 3 * x =', z)
#Part A: the values should be one

TOL = 1e-10
# check if b and f are equal within specified tolerance
if abs(b - f) < TOL:
    print('b and f are equal within tolerance of', TOL)
else:
    print('b and f are NOT equal within tolerance of', TOL)
if abs(b -f) < TOL:
    print('y and z are equal within tolerance of', TOL)
else:
    print('y and z are NOT equal within tolerance of', TOL)


m = 0.1
print('m =', m)
n = 3 * m
print('n = 3 * m = 0.3', n == 0.3)
p = 7 * m
print('p = 7 * m = 0.7', p == 0.7)
q = n + p
print('q = 1', q == 1)