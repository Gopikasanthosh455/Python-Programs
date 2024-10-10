x=[1,2,3,4,5,6,7,8,9]
min=x[0]
for i in range(len(x)):
    if x[i]<min:
        min =x[i]
print("Smallest element is :",min)