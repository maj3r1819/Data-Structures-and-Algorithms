class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
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

    # Create Circular Singly Linked List
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node #node points to itself, hence CSLL
        self.head = node
        self.tail = node
        return "The Circular Single Linked List has been created"

    #Insertion of a Node to the Circular Single Linked List

    def insertCSLL(self,value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode


        else:
            if location ==0: # insert element at the beginning of linked list
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location ==1: # insert element at the end of linked list
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:  #insert node in the middle
                tempNode = self.head
                index = 0
                while index< location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Node has been Successfully inserted!!"

    # Traversing through the circular singly linked list
    def traverseCSLL(self):
        if self.head is None:
            print("Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next: # self.tail.next basically points to head, so if that is head , then---
                    break


    # Delete a Node in the CSLL
    def deleteCSLL(self,location):
        if self.head is None:
            print("Linked List does not exist")

        else:
            if location == 0:  #delete 1st element
                if self.head == self.tail: #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:                       #More than 1 nodes in CSLL
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location == 1: #deletes last element
                if self.head == self.tail: #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:                       #More than 1 nodes in CSLL
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode

            else:
                node = self.head
                index = 0
                while index< location-1:
                    node = node.next
                    index+=1
                nextnode = node.next
                node.next = nextnode.next

    # Search for a Node in the Singly Linked List
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return "Circular Single Linked List Does not Exist :/ "
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return "{} is present in the linked list ".format(node.value)
                node = node.next
                if node == self.tail.next:
                    return "Value does not Exist"

    #Delete entire Linked List
    def deleteEntireCSll(self):
        if self.head is None:
            print("Single Linked List Does not Exist :/ ")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None




circularSLL = CircularSinglyLinkedList()

print("----------------------------")
print("Node Creation")
circularSLL.createCSLL(1)
print([node.value for node in circularSLL])

print("----------------------------")
print("Node Insertion")
circularSLL.insertCSLL(2,1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(3,1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(4,1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(5,1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(0,0)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(6,1)
print([node.value for node in circularSLL])
circularSLL.insertCSLL(10,5)
print([node.value for node in circularSLL])

print("----------------------------")
print("Node Traversal")
circularSLL.traverseCSLL()
print("----------------------------")
print("Node Deletion")
print([node.value for node in circularSLL])
circularSLL.deleteCSLL(0)
print([node.value for node in circularSLL])
circularSLL.deleteCSLL(1)
print([node.value for node in circularSLL])
circularSLL.deleteCSLL(4)
print([node.value for node in circularSLL])


print("----------------------------")
print("Node Search")
print(circularSLL.searchCSLL(5))

print("----------------------------")
print("Deleting and Entire Circular Singly Linked List")
circularSLL.deleteEntireCSll()
print([node.value for node in circularSLL])
