lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

# Arrange in alphabetical order
lucky_numbers.sort()
print(lucky_numbers)

# Reverse the order
lucky_numbers.reverse()
print(lucky_numbers)

#Copy a list
friends2 = friends.copy()
print(friends2)

# Arrange in alphabetical order
friends.sort()
print(friends)

# First line prints list with extension
# Add additional to list
friends.extend(lucky_numbers)
print(friends)

# Second line adds creed at the end of list
friends.append("Creed")
print(friends)

# Third line add Kelly to first numerial spot of list
# Adding element to list based on index listed
friends.insert(1, "Kelly")
print(friends)

# Fourth line removes Jim from List
# Remove item from list
friends.remove("Jim")
print(friends)

# Fifth line removes creed from end of list
# Pops item off the list
friends.pop()
print(friends)

# Finding Kevin and Oscar in list (Searching Index)
# Gives index number
print(friends.index("Oscar"))
print(friends.index("Kevin"))

#Count how many Jims in List
print(friends.count("Jim"))
