try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    result=x/y
    print(result)
except ZeroDivisionError:
    print("Division err,Division by Zero..!")
else:
    print("Successful12 Division....!")