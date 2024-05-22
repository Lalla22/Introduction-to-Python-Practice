"""
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered, unchangeable, and allow duplicate values.
Tuples are declared with parenthesis's. Lists are with square brackets. Used for data that is never going to change. Like coordinates.
"""
# Simple Tuple Example
coordinates = (4, 5)
print(coordinates[0])
print(coordinates[1])

# Creating a list of tuples
coordinates = [(4, 5), (6,7), (89, 34)]
coordinates[1] = 10
print(coordinates[1])


