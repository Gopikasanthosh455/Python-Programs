x=[1,2,3,4,5,6,7,8,9]
max=x[0]
for i in range(len(x)):
    if x[i]>max:
        max =x[i]
print("Largest element is :",max)