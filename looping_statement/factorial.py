x=int(input("Enter a number:"))
if x>0:
    x1=1
    for i in range(1,x+1):
        x1=x1*i
    print("factorial=",x1)
elif x<0:
    print("please enter positive integer")
else:
    print("factorial of zero is one")

