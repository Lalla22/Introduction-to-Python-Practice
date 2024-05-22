"""
Functions are collects of code that perform a specific task
Great for organizing
Can call function to do specific task

"""

# First Function
def say_hi():
    print("Hello User")

# Call function
print("top")
say_hi()
print("bottom")

# Adding parameters to function: Which is giving information to the function
# Can pass in any data for the same result
def sayhi(name, age):
    print("Hello " + name + " you are " + age)

sayhi("Mike", "16")
sayhi("Steve", "10")
