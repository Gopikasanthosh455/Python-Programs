arr = [10, 20, 30, 40, 50]
print("Number of element:",len(arr))
new=[]
for i in range(len(arr)-1,-1,-1):
    new.append(arr[i])
print(new)
    