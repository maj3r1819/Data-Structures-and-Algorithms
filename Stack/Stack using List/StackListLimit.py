"""
ok guys lets learn how to create a stack with a limit!!!
yall with me ????
well
ok
here we go!
stack is a type of a data structure! which follows the first in last out method!!!
yall ready??
k lets go!
so guys! if u create a stack with a list, theres no limit ... now we will create a stack using a list with a max limit
"""

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(value) for value in self.list]
        return "\n".join(values)


    # To check if the stack is empty!

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is Full"
        else:
            self.list.append(value)

    # pop method
    def pop(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            self.list.pop()

    # peek method
    def peek(self):
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            print(self.list[len(self.list) - 1])

    # Delete entire stack
    def delete(self):
        self.list = None

    print("-------------------
customstack =Stack(5)
print(customstack.isEmpty())
print(customstack.isFull())
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
customstack.push(5)
customstack.pop()
customstack.peek()