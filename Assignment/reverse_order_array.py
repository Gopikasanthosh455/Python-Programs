array=[9,7,5,3,1]
new=[]
for i in range(len(array)-1,-1,-1):
    new.append(array[i])
print("Reversed array:",new)
