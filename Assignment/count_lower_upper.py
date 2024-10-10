x=input("Enter a string:")
upper =0
lower=0
for i in x:
    if i.isupper():
        upper+=1
    else:
        lower+=1
print("Number of upper case letters:",upper)
print("Number of lower case letters:",lower)