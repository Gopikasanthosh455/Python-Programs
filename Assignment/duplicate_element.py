array1=[1,2,3,4,5,6,5,4,3,7,8,9]
newlist=[]
for i in range(len(array1)):
    for j in range(i+1,len(array1)):
        if array1[i]==array1[j]:
            newlist.append(array1[i])
print("Duplicate elements :",newlist)
