def calculate_length(n):
    length=0
    while n!=0:
        length+=1
        n=n//10
    return length
num=int(input("Enter a number:"))
x=calculate_length(num)
sum=0
temp=num
while num>0:
    remainder = num%10
    sum = sum +(remainder**x)
    num =num//10
    x-=1
if temp==sum:
    print("Number is Disarium")
else:
    print("Number is not a Disarium number")
