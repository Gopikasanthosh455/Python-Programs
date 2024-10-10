def count_length(n):
    length=0
    while n!=0:
        length+=1
        n//=10
    return length
num=int(input("Enter an integer:"))
print("The total number of digits is :",count_length(num))