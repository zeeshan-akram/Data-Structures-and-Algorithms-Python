class Heap:
    def __init__(self, items=None):
        super().__init__()
        if items is None:
            items = []
        self.heap = []
        for item in items:
            self.heap.append(item)

    def push(self, value):
        self.heap.append(value)
        self.__bubbleup(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def pop(self):
        if len(self.heap) > 0:
            self.__swap(0, len(self.heap) - 1)
            maxi = self.heap.pop()
            self.__bubbledown(0)
        elif len(self.heap) == 0:
            maxi = self.heap.pop()
        else:
            maxi = False
        return maxi

    def findkth(self, num):
        try:
            find = []
            for _ in range(num):
                find.append(self.pop())
            print(find[num-1])
        except IndexError:
            print("we don't have too much data")

    def __swap(self, first, second):
        self.heap[first], self.heap[second] = self.heap[second], self.heap[first]

    def __bubbleup(self, index):
        parent = (index - 1) // 2
        if parent < 0:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__bubbleup(parent)

    def __bubbledown(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__bubbledown(largest)


#numbers = [5, 3, 10, 1, 4, 2]
#heap = Heap()
#for number in numbers:
#    heap.push(number)
#print(str(heap.heap[0:len(heap.heap)]))