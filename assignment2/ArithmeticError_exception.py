try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    result=x/y
    print("division :",result)
except ArithmeticError:
    print("ArithmeticError, An error occurred during the division...!")