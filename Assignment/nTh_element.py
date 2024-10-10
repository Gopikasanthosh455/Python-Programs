mylist = [1,22,333,4444,55555]
n = int(input("Enter the position of the element : "))
if n>0 and n<=len(mylist):
    print("The n-th element is:", mylist[n-1])
else:
    print("The n-th element does not exist in the list.")
