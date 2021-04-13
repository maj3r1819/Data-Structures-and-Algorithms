import sys
sys.path.insert(0, 'D:\Projects\Data-Structures-and-Algorithms\Linked List\Singly Linked List')
from SinglyLinkedListOperations import SLinkedList, Node


def num(linked_list):
    num1 = 0
    if linked_list.head is None:
        return None
    else:
        currNode = linked_list.head
        while currNode:
            val = currNode.value
            num1 = num1*10 + val
            currNode = currNode.next
    return num1
custom_ll = SLinkedList()
custom_ll.insertSLL(1,1)
custom_ll.insertSLL(2,1)
custom_ll.insertSLL(3,1)
custom_ll.insertSLL(3,1)
print("----------------------------------")
print([node.value for node in custom_ll])
print(num(custom_ll))