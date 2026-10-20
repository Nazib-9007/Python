import math;
import random;
x = 10
y = 10.10
z = 10 + 9j
print(type(x), type(y), type(z))

f = '25'
print(type(f))
print(f * 3)
convert = int(f)
print(convert * 3)
print(type(convert))

# Python rounding()
y = 35.6877834
print(f'Before converting y: {y}')
print(f'After use abs(): {abs(y)}')
print(f'After use round(): {round(y)}')
print(f'After use floor(): {math.floor(y)}')
print(f'After use ceil(): {math.ceil(y)}')
print(f'After use trunc(): {math.trunc(y)}')

# Random() and Randint()
a = random.random()
print(f'Random number is: {round(a,2)}')

b = random.randint(1,10)
print(f'The randint number between 1 and 10: {b}')
"""
Challange: Generate a random integer between 1 and 100, and check if the result is an even number?
"""

randNumber = random.randint(1,100)
print(f'The random number is: {randNumber}')
if randNumber % 2 == 0:
    print(f'This is even random number: {randNumber}')
else:
    print(f"It's not even random number: {randNumber}")