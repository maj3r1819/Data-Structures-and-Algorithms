import numpy as np
#1. Missing Number
print("---------------Q1---------------")
mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30]
print("Find missing element between 1 to 30 in the mylist List: ")
n = 30

def missinglist(list , n):
    sum1 = n*(n+1)/2   # sum of n natural numbers formula
    sum2 = sum(list)
    if sum1 == sum:
        return "No missing Number"
    return sum1-sum2
print(missinglist(mylist,n))

#2.
print("---------------Q2---------------")
print("Write a Program to find pairs of integers whose sum is equal to a given number: ")

pairlist  = [2,6,3,9,11]
value = 9
returnlist = []
for i in range(len(pairlist)):
    for j in range(i+1, len(pairlist)):
        if pairlist[i]+ pairlist[j] ==value:
            print([pairlist[i], pairlist[j]])

print("---------------Q3---------------")
print("How to Check if an array contains a number in python: ")
myarray = np.array([1,2,3,4,5,6,7,8,9,10])
value = 5
print("lets implement linear search")
for i in myarray:
    if i == value:
        print("element present")

print("---------------Q4---------------")
print("How to find maximum product of two integers in the array where all the elements are positive: ")
myarray = np.array([10,9,8,7,6,5,4,3,22,1])
prod1= 0
prod2 =0
for i in range(len(myarray)):
    for j in range(i+1, len(myarray)):
        prod1 = myarray[i] * myarray[j]
        if prod1 > prod2:
            prod2 = max(prod1,prod2)

print(prod2)

print("---------------Q5---------------")
print("Is Unique: Implement an Algorithm to determine if a list has all unique characters, using python list: ")

mylist = [1,2,3,4,5,6,7,8,9,9,10,11,1]
a = []
def unique(list):
    for i in mylist:
        if i in a:
            print(i)
            return False
        else:
            a.append(i)
    return True

print(unique(mylist))


print("---------------Q6---------------")
print("Check Permutation: ")
# peek == keep
# rail == liar
# Permutations^

a = 'peek'
b = 'keep'
mylist1 = list(a)
mylist2 = list(b)
mylist2.reverse()
if mylist1 == mylist2:
    print("Permutation found")



print("---------------Q7---------------")
print("Rotate Matrix: ")

myarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original Matrix : \n",myarray)
def rotate(matrix):
    r = len(matrix)
    for layer in range(r//2):
        first = layer    # first =0
        last = r - layer - 1 #last =2
        for i in range(first,last):
            # save top element AKA 1
            top = matrix[layer][i]
            # move 7 in place of 1
            matrix[layer][i] = matrix[-i-1][layer]
            # move 9 in place of 7
            matrix[-i - 1][layer]= matrix[-layer-1][-i-1]
            # move 3 in place of 9
            matrix[-layer - 1][-i - 1] = matrix[i][-layer-1]
            # move 1 in place of 3
            matrix[i][-layer - 1] = top
    return matrix

print("Rotated matrix by 90 degrees:\n", rotate(myarray))