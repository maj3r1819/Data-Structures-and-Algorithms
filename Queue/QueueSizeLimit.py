#Also called as Circular Queue

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None] # To initialize a list with a limit set make a list with the size u want and make all the elements None
        self.maxSize = maxSize
        self.start  = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)


    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start ==0 and self.top+1 == self.top:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full :/")

        else:
            if self.top+1 == self.maxSize: #if queue is not full but top is at the end of the queue it means that we have dequeued elements and now when we enquue elements they will be added at the start of the queu and not the end
                self.top = 0
            else:       #regular adding at the end of the queue
                self.top+=1
                if self.start == -1:
                    self.start=0
            self.items[self.top] = value
            return "Element is inserted at the end of the queue"


    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top: #only 1 element
                self.start = -1
                self.top = -1

            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start+=1
            self.items[start] = None
            return firstelement

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1



customqueue = Queue(3)
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
print(customqueue.dequeue())
print(customqueue)
print(customqueue.peek()) #returns 2 not None wow
