"""
by - majer
ft - Angela and Roache!!
"""

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break


    #Create a Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode

    # Insert Nodes
    def insertCDLL(self, value, location): # so guys in this function we are going to insert a node in our linked list! stay tuned!
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.prev = newNode
            newNode.next = newNode

        else:
            if location == 0: # insert element at the beginning of linked list
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode

            elif location ==1 : # insert element at the end of linked list
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    #Traversal
    def traversalCDLL(self):
        if self.head is None:
            print("Linked List Does not exist :/")

        else:
            node = self.head
            while node:
                print(node.value)
                if node == self.tail:
                    break
                node = node.next

    # Reverse Traversal
    def reversetraversalCDLL(self):
        if self.head is None:
            print("Linked List Does not exist :/")

        else:
            node = self.tail
            while node:
                print(node.value)
                if node == self.head:
                    break
                node = node.prev

    # Search for a Node in the Singly Linked List
    def searchCDLL(self, value):
        if self.head is None:
            return "Circular Single Linked List Does not Exist :/ "
        else:
            node = self.head
            while node:
                if node.value == value:
                    return "{} is present in the linked list ".format(node.value)
                if node == self.tail:
                    return "Value does not Exist"
                node = node.next

    def deleteCDLL(self,location):
        if self.head is None:
            print("Node does not exist "/"")

        else:
            if location ==0 : #delete 1st element
                if self.head == self.tail: #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head.prev =None
                    self.head.next = None
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location ==1:#deletes last element
                if self.head ==self.tail:   #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None

                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index+=1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode

    # Delete entire Linked List
    def deleteEntireCDll(self):
        if self.head is None:
            print("The linked List is Empty :/")
        else:
            self.tail.next = None # deleting reference from the tail node to the head node
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None


circularDLL = CircularDoublyLinkedList()

print("----------------------------")
print("Node Creation")
#circularDLL.createCDLL(1)
print([node.value for node in circularDLL])
"""
Lets go bois we created our Circular Doubly Linked List!!! 
Good job everyone im proud of both you gguyss!!!
"""

print("----------------------------")
print("Node Insertion")
circularDLL.insertCDLL(0,0)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(1,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(2,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(3,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(4,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(5,1)
print([node.value for node in circularDLL])
circularDLL.insertCDLL(10,3)
print([node.value for node in circularDLL])

print("----------------------------")
print("Node Traversal")
circularDLL.traversalCDLL()

print("----------------------------")
print("Node Reverse Traversal")
circularDLL.reversetraversalCDLL()

print("----------------------------")
print("Node Search")
print(circularDLL.searchCDLL(10))

print("----------------------------")
print("Node Deletion")
print("Original Linked List: ")
print([node.value for node in circularDLL])
print("Deletion Operation Starts:")
circularDLL.deleteCDLL(0)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL(1)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL(2)
print([node.value for node in circularDLL])
circularDLL.deleteCDLL(-1)
print([node.value for node in circularDLL])


print("----------------------------")
print("Deleting and Entire Circular Doubly Linked List")
circularDLL.deleteEntireCDll()
print([node.value for node in circularDLL])
