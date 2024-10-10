num= int(input("Enter the number:"))
sum=0
temp=num
while num>0:
    remainder=num%10
    sum+=remainder
    num//=10
if temp%sum==0:
    print("Number is Harshad number")
else:
    print("Number is not a Harshad number")