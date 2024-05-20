"""
Python Data Types: Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
Text type: Str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean types: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType

"""

#string
a = "Hello World"
print(type(a))

#int
b = 20
print(type(b))

#float
c = 20.5
print(type(c))

#complex
d = 1j
print(type(d))

#list
e = ["apple", "banana", "cherry"]
print(type(e))

#tuple
f = ("apple", "banana", "cherry")
print(type(f))

#range
g = range(6)
print(type(g))

#dict
h = {"name" : "John", "age" : 36}
print(type(h))

#set
i = {"apple", "banana", "cherry"}
print(type(i))

#frozenset
j = frozenset({"apple", "banana", "cherry"})
print(type(j))

#bool
k = True
print(type(k))

#bytes
l = b"Hello"
print(type(l))

#bytearray
m = bytearray(5)
print(type(m))

#memoryview
n = memoryview(bytes(5))
print(type(n))

#Nonetype
o = None
print(type(o))

"""
Setting the Specific Data Type
If you want to specify the data type, you can use the following constructor functions:
"""
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list (("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name= "John", age=36)
x = set(("apple", "banana", "cherry"))
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))