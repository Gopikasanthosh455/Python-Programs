num=int(input("please enter a 3 digit number:"))
sum=0
temp=num
while num>0:
    digit=num%10
    sum+=digit**3
    num//=10
if sum==temp:
    print("Number is armstrong number")
else:
    print("Number is not armstrong number")