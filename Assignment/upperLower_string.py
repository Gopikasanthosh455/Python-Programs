def count_upper(n):
    count_upper=0
    for i in n:
        if i.isupper():
            count_upper+=1
    return count_upper
def count_lower(n):
    count_lower=0
    for i in n:
        if i.islower():
            count_lower+=1
    return count_lower
str =input("Enter the string:")

x=count_lower(str)
y=count_upper(str)

print("Number of UPPERCASE latter's  :",y)
print("Number of LOWERCASE latter's  :",x)
