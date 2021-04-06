# List Operations and Functions

# '+' Operator
print('-----------+ Operator------------')
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)
print('----------* Operator--------------')
# '*' Operator
a1 = a * 2
print(a1)
print('--------len function----------------')
print(len(a))
print('--------max function----------------')
print(max(a))
print('--------min function----------------')
print(min(a))
print('--------sum function----------------')
print(sum(a))

print("----------Average--------------")
mylist = []
while(True):
    value = (input("Enter the number: "))
    if value == 'done': break
    value = float(value)
    mylist.append(value)

average = sum(mylist)/len(mylist)
print("Average : ", average)

# Strings and Lists
print("----------Strings to Lists split function--------------")
mystring = 'Sagar Sanjeev Potnis'
print(mystring)
newlist = mystring.split()
print(newlist)
mystring1 = 'Sagar-Sanjeev-Potnis'
print(mystring1)
newlist1 = mystring1.split('-')
print(newlist1)

print("---------- List to String join function--------------")
joinstring = " ".join(newlist)
print(joinstring)
print("----------map function--------------")
print("Please Enter list :")
maplist = list(map(int, input().split()))
print(maplist)
