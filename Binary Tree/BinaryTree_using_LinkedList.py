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

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            else:
                root.value.leftChild = newNode
                return "Successfully Inserted"

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)

            else:
                root.value.rightChild = newNode
                return "Successfully Inserted"

def getDeepestNode(rootNode):
    if not rootNode:
        return

    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)

        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
    if not rootNode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value == deepestNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild ==deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customqueue.enqueue(root.value.rightChild)

            if root.value.leftChild:
                if root.value.leftChild ==deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customqueue.enqueue(root.value.leftChild)


def deleteNode(rootNode, node):
    if not rootNode:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isempty()):
            root = customqueue.dequeue()
            if root.value.data == node:
                deepestNode = getDeepestNode(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNode(rootNode,deepestNode)
                return "Node has been successfully deleted"

            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)

            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)

        return "fail"

def delEnitreBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "Entire BT is deleted!"


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
print("Inserting Node: ")
newnode = TreeNode("Cola")
insertNodeBT(newBT, newnode)
levelOrderTraversal(newBT)

# print("Deepest node is :")
# deepestNode  = getDeepestNode(newBT)
# print(deepestNode.data)
# print("Level order traversal after deleting last node :")
# deleteDeepestNode(newBT, deepestNode)
# levelOrderTraversal(newBT)

print("Deleting given node in a bt:")
deleteNode(newBT, "Hot")
levelOrderTraversal(newBT)

print("Deleting Entire BT:")
print(delEnitreBT(newBT))
levelOrderTraversal(newBT)