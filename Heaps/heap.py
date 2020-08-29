class Heap:
    def __init__(self):
        self.items = []

    def insert(self, value):
        size = len(self.items)
        self.items.insert(size, value)
        if size > 0:
            self.bubbleup()

    def bubbleup(self):
        index = len(self.items) - 1
        parent = self.findparent(index)
        while index > 0 and self.items[parent] < self.items[index]:
            temp = self.items[parent]
            self.items[parent] = self.items[index]
            self.items[index] = temp
            index = parent
            parent = self.findparent(index)

    def findparent(self, index):
        parent = (index - 1) // 2
        return parent

    def remove(self):
        index = len(self.items) - 1
        self.items[0] = self.items.pop(index)
        self.bubbledown()

    def bubbledown(self):
        index = 0
        while index <= (len(self.items)-1) and not self.isValidParent(index):
            largerchild = self.largerChildIndex(index)
            self.items[index], self.items[largerchild] = self.items[largerchild], self.items[index]
            index = largerchild

    def isValidParent(self, index) -> bool:
        if not self.hasLeftChild(index):
            return True
        isValid = self.items[index] >= self.leftChild(index)
        if not self.hasRightChild(index):
            isValid &= self.items[index] >= self.rightChild(index)
        return isValid

    def largerChildIndex(self, index):
        if not self.hasLeftChild(index):
            return index
        if not self.hasRightChild(index):
            return self.leftChildIndex(index)
        return self.leftChildIndex(index) \
            if self.leftChild(index) > self.rightChild(index) \
            else self.rightChildIndex(index)

    def hasLeftChild(self, index) -> bool:
        return self.leftChildIndex(index) <= len(self.items) - 1

    def hasRightChild(self, index) -> bool:
        return self.rightChildIndex(index) <= len(self.items) - 1

    def leftChild(self, index):
        return self.items[self.leftChildIndex(index)]

    def rightChild(self, index):
        return self.items[self.rightChildIndex(index)]

    def leftChildIndex(self, index):
        return index * 2 + 1

    def rightChildIndex(self, index):
        return index * 2 + 2


    def display(self):
        print(self.items)

heap = Heap()
heap.insert(5)
heap.insert(3)
heap.insert(10)
heap.insert(1)
heap.insert(4)
heap.insert(2)
heap.display()
heap.remove()
heap.remove()
heap.display()