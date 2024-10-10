from math import sqrt
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

r=(b**2)-4*a*c
if r<0:
    print("discriminant less than zero")
elif r>0:
    x1=((-b)+(sqrt(r)))/2*a
    x2=((-b)-(sqrt(r)))/2*a
    print("two result are",x1 ,"and",x2)
else:
    x3=-b/2*a
    print("result=",x3)