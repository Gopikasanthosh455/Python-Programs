import re

#replacing one or many matches with a string
mystring="introduction to regular expression in python"
x=re.sub(r"\s","_",mystring)

print(x)