import sys
sys.path.insert(0, 'D:\Projects\Data-Structures-and-Algorithms\Linked List\Singly Linked List')
from SinglyLinkedListOperations import SLinkedList, Node

#Implement and algorithm to find the nth to last element of a singly linked list
def nth2last(linked_list, n):
    pointer1 = linked_list.head
    pointer2 = linked_list.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1.value

custom_ll = SLinkedList()
custom_ll.insertSLL(0,1)
custom_ll.insertSLL(1,1)
custom_ll.insertSLL(2,1)
custom_ll.insertSLL(3,1)
custom_ll.insertSLL(4,1)
print("----------------------------------")
print("Practice Question Starts!")
print("Original Linked List: ")
print([node.value for node in custom_ll])
print(nth2last(custom_ll,3))

