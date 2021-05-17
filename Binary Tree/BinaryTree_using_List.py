class BinaryTree:
    def __init__(self, size):
        self.customList = size* [None]
        self.lastUsedIndex = 0
        self.maxSize = size


    def insertNode(self, value):
        if self.lastUsedIndex +1 == self.maxSize:
            return "Binary Tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1
        return "The Value has been inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)


    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
            if index > self.lastUsedIndex:
                return
            self.postOrderTraversal(index * 2)
            self.postOrderTraversal(index * 2 + 1)
            print(self.customList[index])

    def levelOrderTraversal(self,index):
        for i in range(index, self.lastUsedIndex+1):
             print(self.customList[i])




newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
print(newBT.searchNode("Cold"))
newBT.preOrderTraversal(1)
print("-----------------")
newBT.inOrderTraversal(1)
print("-----------------")
newBT.postOrderTraversal(1)
print("-----------------")
newBT.levelOrderTraversal(1)
print("-----------------")
