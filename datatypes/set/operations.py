set1={"nisha","nimisha","Gopika","devika","anu","Gopika","paru",}
set2={"anu","malu"}

print("union operation using union() method")
print(set1.union(set2))
print("union operation using pipe | operator")
print(set1 | set2)

print("intersection operation using intersection() method")
print(set1.intersection(set2))
print("intersection operation using and & operator")
print(set1 & set2)

print("difference operation using difference() method")
print(set1.difference(set2))
print("difference operation using - operator")
print(set1 - set2)

print("symmetric difference operation using symmetric difference() method")
print(set1.symmetric_difference(set2))
print("symmetric difference operation using ^ operator")
print(set1 ^ set2)