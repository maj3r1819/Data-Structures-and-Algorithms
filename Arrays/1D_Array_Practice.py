from array import *

# 1 Create Array and Traverse

myarray = array('i', [1,2,3,4,5])
for i in myarray:
    print(i)

# 2 Acess Individual Elements through indexes
print("Step 2")
print(myarray[0])

# 3 Append element
print("Step 3")
myarray.append(6)
print(myarray)

# 4 insert method
print("Step 4")
myarray.insert(0, 0)
print(myarray)

# 5 Extend array
print("Step 5")
myarray1 = array('i', [7,8,9,10])
myarray.extend(myarray1)
print(myarray)

# 6 Add items from list into arrays
print("Step 6")
mylist = [11,12,13]
myarray.fromlist(mylist)
print(myarray)

# 7 remove element
print("Step 7")
myarray.remove(13)
print(myarray)

# 8 pop
print("Step 8")
myarray.pop()
print(myarray)

# 9 fetch value using index
print("Step 9")
print(myarray.index(10))

# 10 reverse
print("Step 10")
myarray.reverse()
print(myarray)

# 11 buffer
print("Step 11")
print(myarray.buffer_info())

#12 count
print("Step 12")
myarray.append(0)
print(myarray)
print(myarray.count(0))

#13 convert to string
'''
print("Step 13")
mystring  = myarray.tostring()
print(myarray)
'''
#14 convert to string
print("Step 14")
#print(myarray.tolist())

#15 slicing
print("Step 15")
print(myarray[1:5])

