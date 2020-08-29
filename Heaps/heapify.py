class Heapify:
    def __init__(self, items=None):
        super().__init__()
        self.heap = []
        for i in range(len(items)):
            self.heap.append(items[i])

    def insert(self, items):
        self.heap.append(items)
        self.heapify()

    def heapify(self):
        for i in range((len(self.heap)//2)):
            left = (i * 2) + 1
            right = (i * 2) + 2
            if self.__validchild(left) and self.__Leftchild(i, left, right):
                self.__swap(i, left)
            elif self.__validchild(right) and self.__Rightchild(i, right):
                self.__swap(i, right)

    def __validchild(self, child):
        return child < len(self.heap) - 1

    def __Rightchild(self, parent, right) -> bool:
        return self.heap[parent] < self.heap[right]

    def __Leftchild(self, parent, left, right) -> bool:
        return self.heap[parent] < self.heap[left] > self.heap[right]

    def __swap(self, i, child):
        self.heap[i], self.heap[child] = self.heap[child], self.heap[i]


heapify = Heapify([5, 3, 8, 4, 1, 2])
heapify.heapify()
print(str(heapify.heap[0:len(heapify.heap)]))