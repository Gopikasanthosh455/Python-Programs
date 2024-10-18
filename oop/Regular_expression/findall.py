import re

#returns a list containing every occurrence of "t0"
mystring="introduction to regular expression in python"
a=re.findall("to",mystring)
print(a)
print(type(a))
print(len(a))