import sys
sys.path.insert(0, 'D:\Projects\Data-Structures-and-Algorithms\Queue')
from QueueLinkedList import Queue
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)



print("Pre Order Traversal: ")
preOrderTraversal(newBT)
print("In Order Traversal: ")
inOrderTraversal(newBT)
print("Post Order Traversal: ")
postOrderTraversal(newBT)
print("Level Order Traversal: ")
levelOrderTraversal(newBT)
