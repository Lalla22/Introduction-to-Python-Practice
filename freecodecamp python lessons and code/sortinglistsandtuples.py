# Sorting Lists of Tuples
# Using the sorted method
# Same code written in different way
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

print( sorted( [(v, k) for k, v in counts.items()], reverse=True ) )
