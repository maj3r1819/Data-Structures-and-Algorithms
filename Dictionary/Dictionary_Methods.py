# Dictionary Methods

# 1. Clear method

sagardict = {"name": "Sagar", "age": 20, "address": "Pune", "education": "Engineer"}
sagardict.clear()
print(sagardict)
print("------------------------------")

#Copy Method
sagardict = {"name": "Sagar", "age": 20, "address": "Pune", "education": "Engineer"}

copydict = sagardict.copy()
print(copydict)
print("------------------------------")


# Fromkeys method
newdict = {}.fromkeys([1,2,3], "hello")
print(newdict)
print("------------------------------")


# get method

print(sagardict.get("name"))
print("------------------------------")

# items method
print(sagardict.items())
print("------------------------------")


# keys method
print(sagardict.keys())
print("------------------------------")

# set default method
sagardict.setdefault("sport", "table tennis")
print(sagardict)
print("------------------------------")

# values method

print(sagardict.values())
print("------------------------------")

#Update method
newdict = {"a": 1, "b":2, "c": 3}
sagardict.update(newdict)
print(sagardict)