def factorial_recursion(n):
    if n==1:
        return n
    else:
        return n*factorial_recursion(n-1)
num= int(input("Enter a number:"))
if num==0:
    print("Factorial of ZERO is ONE")
elif num<0:
    print("Please enter a positive integer")
else:
    print("Factorial  :",factorial_recursion(num))