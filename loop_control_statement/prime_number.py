num=int(input("Enter a number:"))
if num<0:
    print("please enter a positive number")
elif num==0:
    print("you have entered zero")
elif num==1:
    print("zero is composite number")
else:
    for i in range(2,num):
        if num%2==0:
            print("number is not prime number")
            break
    else:
        print("number is a prime number")