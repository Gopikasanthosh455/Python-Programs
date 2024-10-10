try:
    x=int(input("Enter first number:"))
    y=int(input("Enter second number:"))
    result=x/y
    print(result)
except:
    print("Error occured...!")
finally:
    print("Division completed")