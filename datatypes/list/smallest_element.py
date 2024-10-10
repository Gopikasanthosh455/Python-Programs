x=[1,2,22,3,2,4]
min=x[0]
for i in range(len(x)):
    if x[i]<min:
        min=x[i]
print("smallest element is:",min)