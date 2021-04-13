"""
No size limit in this case
"""
class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    # isEmpty method checks if stack is empty or not
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False

    #push method
    def push(self, val):  #time Complexity for .append() is O(n) not O(1)
        self.list.append(val)
        print("{} has been inserted!".format(val))

    #pop method
    def pop(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            self.list.pop()

    #peek method
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            print(self.list[len(self.list)-1])

    #Delete entire stack
    def delete(self):
        self.list = None
print("---------------------")
print("isEmpty method:")
customstack = Stack()
print(customstack.isEmpty())
print("---------------------")
print("Push method:")
customstack.push(0)
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print("---------------------")
#print(customstack)
print("---------------------")
customstack.pop()
#print(customstack)
"""
print(customstack) calls the __str__ method again and again and reverses the list evreytime 
so make sure to call it only once and comment the rest
"""
print("---------------------")
print("Peek method:")
customstack.peek() #had to comment both the print(customstack) because without doing so wouldve peaked the wrong element
print("---------------------")
