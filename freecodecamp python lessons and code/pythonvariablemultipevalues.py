"""
Python allows you to assign values to multiple variables in one line:
And you can assign the same value to multiple variables in one line:
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
"""

#Example
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Example
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome "
print(x + y + z)

"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.
Global variables can be used by everyone, both inside of functions and outside.

"""

#Example
x = "awesome"
def myfunc():
    print("Python is " + x)

myfunc()

#Example
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
To create a global variable inside a function, you can use the global keyword.
"""
#Example
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# Use the global keyboard if you want to change a global variable inside a function
# To change the value of a global variable inside a function, refer to the variable by using the global keyword
#Example
x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)

