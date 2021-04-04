import numpy as np


# Create 2D array
twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("-----------1------------")

print(twoDarray)
print("------------2-----------")

# Insert column
newtwoDarray = np.insert(twoDarray, 0, [[0, 0, 0]], axis = 1) # in axis 1 is coloum and 0 is row
print(newtwoDarray)
newtwoDarray = np.append(twoDarray,[[0, 0, 0]], axis = 0) # appends in the end
print("----------3-------------")
print(newtwoDarray)

# Access Elements
print("-----------4------------")
print(newtwoDarray[0][2])

# Array Traversal
print("----------5-------------")
for i in range(len(newtwoDarray)): # u dont pass anything, it passes 1 by default aka the row
    for j in range(len(newtwoDarray[0])):
        print(newtwoDarray[i][j])
print("-----------6------------")

# searching element thru linear search
def search(arr, value):
    for i in range(len(arr)): # u dont pass anything, it passes 1 by default aka the row
        for j in range(len(arr[0])):
            if value == arr[i][j]:
                print("Element found at : ", i,j)
search(twoDarray, 6)

#delete a column or row
print("----------7-------------")
newarr = np.delete(newtwoDarray, 0,axis = 0)
print(newarr)