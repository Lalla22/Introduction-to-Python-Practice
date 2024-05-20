lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
# First line prints list with extension
friends.extend(lucky_numbers)
print(friends)

# Second line adds creed at the end of list
friends.append("Creed")
print(friends)

# Third line add Kelly to first numerial spot of list
friends.insert(1, "Kelly")
print(friends)

# Fourth line removes Jim from List
friends.remove("Jim")
print(friends)

# Fifth line removes creed from end of list
friends.pop()
print(friends)

# Finding Kevin and Oscar in list (Searching Index)
print(friends.index("Oscar"))
print(friends.index("Kevin"))

#Count how many Jims in List
print(friends.count("Jim"))

# Arrange in alaphebical order