class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def Enqueue(self, value):
        self.items.append(value)
        return "Element is inserted at the end of the Queue"

    def Dequeue(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
            return self.items.pop(0)

    def Peek(self):
        if self.isEmpty():
            return "There is no element in the Queue"
        else:
             return self.items[0]


    def Delete(self):
        self.items = None
        
customqueue = Queue()
print(customqueue.isEmpty())
customqueue.Enqueue(1)
customqueue.Enqueue(2)
customqueue.Enqueue(3)

print(customqueue.Dequeue())
print(customqueue)