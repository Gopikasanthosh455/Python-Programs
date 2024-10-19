def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
if num<0:
    print("Please enter a positive integer..!")
elif num==0:
    print("Factorial of ZERO is ONE")
else:
    print("Factorial :",factorial(num))



