# 1 Create a list
intlist = [1,2,3,4,5]
stringlist = ['s','a','g','a','r']
mixedlist = [1, 2.5, 'sagar']
nestedlist = [1,2,3,[5,6,7]]

# 2 Accessing elements in list
shopping_list = ['milk', 'cheese', 'butter']
for i in shopping_list:
    print(i)
print('------------------------------')
print('milk' in shopping_list)
print('------------------------------')


# 3 Update

mylist = [1,2,3,4,5,6]
print(mylist)
mylist[1] = 1.5
print(mylist)
print('------------------------------')


#4 Insert
mylist.insert(2, 2)
print(mylist)
mylist.insert(4, 3.5)
print(mylist)
mylist.append(7)
print(mylist)
newlist = [8,9,10]
mylist.extend(newlist)
print(mylist)
print('------------------------------')

#5 deleting and slicing
strlist = ['a','b','c','d']
print(strlist[0:2])
strlist[0:2] = ['x', 'y']
print(strlist)
strlist.pop(0) # not passing index will pop the last element
print(strlist)
del strlist[0:2]
print(strlist)
strlist.append('a')
strlist.append('b')
strlist.append('c')
print(strlist)
strlist.remove('d')
print(strlist)
print('------------------------------')

# 6 Searching for an element in a List
mylist1 = [1,2,3,4,5,6,7,8,9,10]

if 2 in mylist1:
    print(mylist1.index(2))
else:
    print("value does not exist")
print('------------------------------')

def linearsearch(list, value):
    for i in list:
        if i == value:
            return list.index(value)

    return "value does not exist"
print(linearsearch(mylist1, 5))
print('------------------------------')

