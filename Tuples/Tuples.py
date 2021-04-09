#Creating a Tuple

newtuple = 'a','b','c','d'
print(newtuple)
# Tuple with 1 element
tupple = 'a',
print(tupple)
newtuple1 = tuple('abcd')
print(newtuple1)
print("------------------")

#Accessing Tuples
newtuple = 'a','b','c','d'
print(newtuple[1])
print(newtuple[-1])

#Traversing a Tuple

for i in newtuple:
    print(i)
print("------------------")

#Searching a tuple

print('b' in newtuple)