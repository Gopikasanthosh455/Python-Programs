def count_length(x):
    length=0
    while(x != 0):
        length +=1
        x = x//10
    return length
num=int(input("Enter a number : "))
x=count_length(num)
print("Length of the given number is :",x)
sum=0
a = num
while num>0:
    reminder = num%10
    sum =sum+(reminder**x)
    num =num//10
    x -=1

if a==sum:
    print("Number is Disarium ")
else:
    print("Number is not Disarium")