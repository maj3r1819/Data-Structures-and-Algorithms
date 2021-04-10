class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    # Insertion in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        # Check if node is empty, if it is empty set new node as head and tail
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location ==0: # insert element at the beginning of linked list
                newNode.next = self.head # why? because head stores adress of the newNode
                self.head = newNode
            elif location ==1: # insert element at the end of linked list
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else: #insert node in the middle
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traversing Through the Linked List!!
    def traverseSLL(self):
        if self.head is None:
            print("Single Linked List Does not Exist :/ ")

        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next


singlylinkedlist = SLinkedList()

print("----------------------------")
print("Node Insertion")
singlylinkedlist.insertSLL(1,0)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL(3,1)
singlylinkedlist.insertSLL(4,1)
singlylinkedlist.insertSLL(5,2)

print([node.value for node in singlylinkedlist])
print("----------------------------")
print("Node Traversal")
singlylinkedlist.traverseSLL()






