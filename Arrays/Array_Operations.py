from array import *

##################################################################
# 1. Create an array and traverse.
myarray = array('i', [1,2,3,4,5,6]) # i means int
print(myarray)
myarray1 = array('d', [1.3,2.4,3.2,4.1,5.5]) # d means double
print(myarray1)
##################################################################
# 2. Insert Elements in an array.
myarray.insert(6, 7) #6 is the index and 7 is the value
print(myarray)
myarray.insert(0, 0) #6 is the index and 7 is the value
print(myarray)
##################################################################
# 3 Traversal Operations
def traverse(array):
    for i in array:
        print(i)
traverse(myarray)
##################################################################
print("--------------------------------")
# 4 Accessing an element in an array
def accesselement(arr, index):
    if index>= len(arr):
        print("No such element present")
    print(arr[index])
accesselement(myarray, 4)
##################################################################
print("--------------------------------")
# 5 Searching for an element
def search(arr , value):
    for i in arr:
        if i == value:
            print("Element present at :", arr.index(value))
search(myarray, 4)
##################################################################
print("--------------------------------")

