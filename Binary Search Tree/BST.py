import sys
sys.path.insert(0, 'D:\Projects\Data-Structures-and-Algorithms\Queue')
from QueueLinkedList import Queue
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):   ###### Not your code######
    if rootNode.data == None:
        rootNode.data = nodeValue

    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)

    elif nodeValue> rootNode.data:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "Node is successfully Intersted"

def insertNode1(rootNode, nodeValue):   #####new insertion method , your idea,,, non recursive #####
    if rootNode.data is None:           #### CORRECTION, this function does not create a proper BST
        rootNode.data = nodeValue
        return "Node is successfully Inserted"

    elif nodeValue <= rootNode.data:
        while rootNode.leftChild is not None:
            rootNode = rootNode.leftChild
        rootNode.leftChild = BSTNode(nodeValue)
        return "Node is successfully Inserted"

    elif nodeValue>= rootNode.data:
        while rootNode.rightChild is not None:
            rootNode = rootNode.rightChild
        rootNode.rightChild = BSTNode(nodeValue)
        return "Node is successfully Inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isempty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)




newBST = BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,50))
print(insertNode(newBST,90))
print(insertNode(newBST,30))
print(insertNode(newBST,60))
print(insertNode(newBST,80))
print(insertNode(newBST,100))
print(insertNode(newBST,20))
print(insertNode(newBST,40))
# print(newBST.leftChild.data)
# print(newBST.rightChild.data)
print("-----------------PreOrderTraversal-------------------")
preOrderTraversal(newBST)
print("-----------------InOrderTraversal-------------------")
inOrderTraversal(newBST)
print("-----------------PreOrderTraversal-------------------")
postOrderTraversal(newBST)
print("-----------------LevelOrderTraversal-------------------")
levelOrderTraversal(newBST)





