month={"january","february","march","april","may","june","july","august"}
print(month)
month.add("september")
print(month)
month.update(["october","november","december"])
print(month)

month.remove("december")
print(month)
month.discard("july")
print(month)


del month
#print(month)