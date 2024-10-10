def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("A.Addition")
print("B.Subtraction")
print("C.multiplication")
print("D.Division")
choice=input("Enter your choice:")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if choice=="A" or choice=='a':
    print("Sum =",addition(num1,num2))
elif choice=="B" or choice=="b":
    print("Difference =",subtraction(num1,num2))
elif choice=="C" or choice=="c":
    print("Product =",multiplication(num1,num2))
elif choice=="D" or choice=="d":
    print("Division =",division(num1,num2))
else:
    print("Invalid Choice....")
