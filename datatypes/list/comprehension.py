mylist=["Abiram","Gopika","vipin","sooraj","Ajil","Rohit"]
newlist=[]
for i in mylist:
    if "A" in i or "a" in i:
        newlist.append(i)
print(newlist)


print("---using compresion---")
first=["Abiram","Gopika","vipin","sooraj","Ajil","Rohit"]
new=[x for x in first if "a" in x or "A" in x]
print(new)