class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.customlist = [0] * (self.numberstacks*self.numberstacks)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize
         