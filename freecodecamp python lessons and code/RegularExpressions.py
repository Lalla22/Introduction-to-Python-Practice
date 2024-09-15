# Regular Expressions


# Before you use regular expressions in your program, you must import the library using import re
# You can use re.search() to see if a string matches a regular expression, similar to using the find() method for string
# Which regex matches only a white space character: /s

# Matching and Extracting Data
# re.search() returns a True/False depending on whether the string matches the regular expression
# if we actually want to matching strings to be extracted we use re.findall

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
print(lst)
