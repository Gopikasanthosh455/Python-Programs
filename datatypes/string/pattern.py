# str = input("Enter a string:")
# for i in range(1, len(str) + 1):
#     print(str[0:i])
#

str ="python"
x=len(str)
for i in range(len(str)):
    for j in range(i+1):
        print(str[j],end=" ")
    print()