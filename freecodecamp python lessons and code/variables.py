"""
Variables are containers for storing data
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it.
Variables do not need to be declared with any particular type, and can even change type after they have been set.
If you want to specify the data type of a variable, this can be done with casting.
Variable names are case-sensitive.
"""

#Variable Exercises
character_name = "Sammy"
character_age = "50"
is_male = False
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

character_name = "Mike"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age )

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#Get the type
print(type(x))
print(type(y))
print(type(z))

