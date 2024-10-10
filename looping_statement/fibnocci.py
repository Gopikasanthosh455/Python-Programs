
n = int(input("Enter the limit:"))
a=0
b=1
print(a)
print(b)
for i in range(3,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum)