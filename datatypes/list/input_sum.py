n=int(input("Enter the number of element:"))
newlist=[]
print("Enter the element:")
for i in range(n):
    element=int(input())
    newlist.append(element)
sum=0
for i in newlist:
    sum +=i
print("Sum of elements:",sum)

