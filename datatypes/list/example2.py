array1=[1,2,3,4,5,6,7,1,22,9,80,56,2,3,4,5]
newlist =[]
for i in range(len(array1)):
    for j in range(i+1,len(array1)):
        if array1[i]==array1[j]:
            newlist.append(array1[i])
print(newlist)