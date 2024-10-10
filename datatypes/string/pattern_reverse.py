str = "python"
x = len(str)
for i in range(x):
    for j in range(i+1):
        print(str[j], end=" ")
    print()
#
# for i in range(x):
#     for j in range(x-i-1, -1, -1):
#         print(str[j], end=" ")
#     print()
for a in range(x,0,-1):
    for b in range(a-1):
        print(str[b],end=" ")
    print()
        