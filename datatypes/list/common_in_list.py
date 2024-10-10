list1 = [1, 2, 3, 4, 5,2,1]
list2 = [6, 7, 8, 1,2,1]
newlist=[]
for i in list1:
    for j in list2:
       if i==j and i not in newlist:
           newlist.append(i)
print(newlist)
