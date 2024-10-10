def count_length(x):
    length=0
    while(x != 0):
        length +=1
        x = x//10
    return length
num=int(input("Enter a number : "))
print("Length of the given number is :",count_length(num))