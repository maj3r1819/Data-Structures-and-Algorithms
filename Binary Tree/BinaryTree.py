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
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
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


def searchTree(rootNode, nodeValue):
    if not rootNode:
        return "Bt does not exist"
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not (customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.data == nodeValue:
                return "Success, Node found : {}".format(nodeValue)
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
        return "Not Found"

print("Pre Order Traversal: ")
preOrderTraversal(newBT)
print("In Order Traversal: ")
inOrderTraversal(newBT)
print("Post Order Traversal: ")
postOrderTraversal(newBT)
print("Level Order Traversal: ")
levelOrderTraversal(newBT)
print("Searching Node: ")
print(searchTree(newBT, "Tea"))

