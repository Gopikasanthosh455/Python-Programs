str=input("Enter a string:")
lower_count=0
upper_count=0
for i in str:
    if i.islower():
        lower_count += 1
    else:
        upper_count += 1

print("Lowercase count:",lower_count)
print("Uppercase count:",upper_count)