def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
choice=int(input("Enter your choice (1/2/3/4):"))
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice==1:
    print("sum  =",addition(num1,num2))
elif choice==2:
        print("Difference  =",subtraction(num1,num2))
elif choice==3:
        print("Product  =",multiplication(num1,num2))
elif choice==4:
        print("Division =",division(num1,num2))
else:
        print("Invalid Choice")
