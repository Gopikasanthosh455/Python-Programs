English=float(input("Enter marks for English:"))
Maths=float(input("Enter marks for Maths:"))
Computer=float(input("Enter marks for Computer:"))
physics=float(input("Enter marks for physics:"))
chemistry=float(input("Enter marks for chemistry:"))
total=English+Maths+Computer+physics+chemistry
print("Total marks  :",total)
percentage=(total/500)*100
print("Percentage  :",percentage)

if percentage>=90:
    print(" A Grade")
elif percentage>=80:
    print(" B Grade")
elif percentage>=70:
    print(" C Grade")
elif percentage>=60:
    print(" D Grade")
else:
    print(" Failed")
