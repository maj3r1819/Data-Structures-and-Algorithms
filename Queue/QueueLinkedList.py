class Node:
    def __init__(self,value):
        self.value  = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode

        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode

    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isempty():
            return "Queue is empty"

        else:
            tempnode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return tempnode

    def peek(self):
        if self.isempty():
            print("there are no nodes in the quuee")

        else:
            print(self.linkedlist.head)

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


customqueue = Queue()
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue)
print(customqueue.dequeue())
print(customqueue)
customqueue.peek()