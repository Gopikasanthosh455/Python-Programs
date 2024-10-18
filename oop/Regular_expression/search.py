import re
mystring="introduction to regular expression in python"
#returns a match object if there is a match anywhere in the string
x=re.search("to",mystring)
print(x)
print(mystring.index("to"))