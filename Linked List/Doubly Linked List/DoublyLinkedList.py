class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "DLL is Created Successfully!"

    # Create Circular Singly Linked List
    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode

        else:
            if location == 0:  # insert element at the beginning of linked list
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

            elif location ==1: # insert element at the end of linked list
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

            else:  # insert node in the middle
                tempNode = self.head
                index = 0
                while index<location-1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = None
                nextNode.prev = None
                newNode.next = nextNode
                nextNode.prev = newNode
                newNode.prev = tempNode
                tempNode.next = newNode

                """
                #Without creating a new node called NextNode^^^ like above, this method is more efficient but not mine :(
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
                """
    # Traversing through the  Doubly linked list
    def traverseDLL(self):
        if self.head is None:
            print("Linked List does not exist")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def reversetraverseDLL(self):
        if self.tail is None:
            print("Linked List does not exist")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev

    #Searching an element in linked list
    def searchDLL(self,nodeValue):
        if self.head is None:
            return "Linked List does not exist"
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return "{} is present in the linked list ".format(node.value)
                node = node.next
        return "Value does not Exist"

    #Deleting an element in the linked list
    def deleteDLL(self,location):
        if self.head is None:
            print("Linked List does not Exist :/")

        else:
            if location ==0: #delete 1st element
                if self.head == self.tail: #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head = None
                    self.tail = None

                else:
                    self.head = self.head.next
                    self.head.prev = None

            elif location ==1: #deletes last element
                if self.head ==self.tail:   #checking if there is only 1 Node ie if both head and tail reference to the same node
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev #we dont have to traverse through the entire linked list unlike SLL and CSLL
                    self.tail.next = None

            else:
                curNode = self.head
                index = 0
                while index < location -1:
                    curNode = curNode.next
                    index+=1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode

    # Delete entire Linked List
    def deleteEntireDll(self):
        if self.head is None:
            print("The linked List is Empty :/")

        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None





doublylinkedlist = DoublyLinkedList()

print("----------------------------")
print("Node Creation")
doublylinkedlist.createDLL(0)
print([node.value for node in doublylinkedlist])

print("----------------------------")
print("Node Insertion")
doublylinkedlist.insertDLL(1,1)
print([node.value for node in doublylinkedlist])
doublylinkedlist.insertDLL(2,1)
print([node.value for node in doublylinkedlist])
doublylinkedlist.insertDLL(3,1)
print([node.value for node in doublylinkedlist])
doublylinkedlist.insertDLL(4,1)
print([node.value for node in doublylinkedlist])
doublylinkedlist.insertDLL(10,2)
print([node.value for node in doublylinkedlist])

print("----------------------------")
print("Node Traversal")
doublylinkedlist.traverseDLL()
print("----------------------------")
print("Node Reverse Traversal")
doublylinkedlist.reversetraverseDLL()

print("----------------------------")
print("Node Search")
print(doublylinkedlist.searchDLL(10))

print("----------------------------")
print("Node Deletion")
print("Original Linked List: ")
print([node.value for node in doublylinkedlist])
doublylinkedlist.deleteDLL(0)
print([node.value for node in doublylinkedlist])
doublylinkedlist.deleteDLL(1)
print([node.value for node in doublylinkedlist])
doublylinkedlist.deleteDLL(2)
print([node.value for node in doublylinkedlist])
doublylinkedlist.deleteDLL(-100)    #To delete negative value pass any negative value
print([node.value for node in doublylinkedlist])

print("----------------------------")
print("Deleting and Entire Doubly Linked List")
doublylinkedlist.deleteEntireDll()
print([node.value for node in doublylinkedlist])



