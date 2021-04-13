import sys
sys.path.insert(0, 'D:\Projects\Data-Structures-and-Algorithms\Linked List\Singly Linked List')
from SinglyLinkedListOperations import SLinkedList, Node


#Method to delete duplicates in a Linked List
def remove_duplicates(linked_list):
    if linked_list.head is None:
        return
    else:
        currNode = linked_list.head
        visited_set = {currNode.value}
        while currNode.next:
            if currNode.next.value in visited_set:
                currNode.next = currNode.next.next
            else:
                visited_set.add(currNode.next.value)
                currNode = currNode.next

    return linked_list

custom_ll = SLinkedList()
custom_ll.insertSLL(0,1)
custom_ll.insertSLL(1,1)
custom_ll.insertSLL(2,1)
custom_ll.insertSLL(3,1)
custom_ll.insertSLL(3,1)
print("----------------------------------")
print("Practice Question Starts!")
print("Original Linked List: ")
print([node.value for node in custom_ll])
remove_duplicates(custom_ll)
print("Linked List after deleting duplicates: ")
print([node.value for node in custom_ll])


