from math import *
import random

print(-2.0987)
print(2)
print(3 * 4.5)
print(3+4)
print(3 * 5 + 5)
print(3* (4 +5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num))
print(str(my_num) + " my favorite number")

my_num = -5
print(abs(my_num))
print(pow(3, 2))
print(pow(4, 6))
print(max(4, 6))
print(min(4, 6))
print(round(4, 6))
print(round(3.2))
print(round(3.7))
print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

# Complex Numbers
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Converting Types
# You can convert from one type to another with the int(), float(), and complex() methods.
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number
# Python has a built-in module called random that can be used to make random numbers:
print(random.randrange(1, 10))