class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:
    def __init__(self):
        self.linkedlist = SLinkedList()  #stackobj.linklist

    def __str__(self):
        values = [str(x.value) for x in self.linkedlist]
        return "\n".join(values)

    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        return False

    def push(self, value):
        node = Node(value)
        node.next = self.linkedlist.head
        self.linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            return "There is no element in Stack"
        else:
            nodevalue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodevalue

customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack)
print("-----------------")
customstack.pop()
print(customstack)


