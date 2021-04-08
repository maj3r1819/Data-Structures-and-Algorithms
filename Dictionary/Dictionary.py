#Creating a Dictionary

# Dictionaries are unordered collections , so the order of a dictionary can change while printing !

myDict = {}   # create a dictionary or by using dict()
eng2spn = {"one" : "uno", "two" : "dos", "three" : "tres"}
print("------------------------------")
print(eng2spn)
print(eng2spn["one"])
'''
Dictionaries work on the concept of hash maps and hash functions.
when we pass the key "one" in the dictionary.. it passed the key
ie "one" to the hash function. the hash function then searches for 
the index of the array of the key and returns the value of the key
aka "one"
flow: 
when eng2spn["one"] is called ----> hash("one") ---> looks for index -----> returns "uno"
'''

print("------------------------------")
# Update/ Add element to a Dictionary

sagardict = {"name": "Sagar", "age": 20}
sagardict["age"] = 21
print(sagardict)
sagardict["address"] = "Pune"
print(sagardict)
print("------------------------------")


# Traverse through a Dictoionary
def Traverse(dict):
    for key in dict:
        print(key, dict[key])


Traverse(sagardict)


#Search for an element
print("------------------------------")
def Search(dict , value):
    for key in dict:
        if dict[key] == value:
            return "value Present"


    return "value not Present"


print(Search(sagardict, "Pune"))


#Delete an element from Dictionary
print("------------------------------")
sagardict = {"name": "Sagar", "age": 20, "address": "Pune", "education": "Engineer"}
sagardict.pop("address")
print(sagardict)

del sagardict["education"]
print(sagardict)
#.popitems() deletes any random key,, clear() clears entire dictionary