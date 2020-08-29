class CheckMaxheap:
    def __init__(self, items=None):
        super().__init__()
        if items is None:
            items = []
        self.heap = []
        for item in items:
            self.heap.append(item)

    def push(self, value):
        self.heap.append(value)

    def ismaxheap(self):
        for i in range(len(self.heap)):
            if self.__ismaxparent(i):
                maxheap = True
            elif self.__isminparent(i):
                maxheap = False
            if not maxheap:
                break
        return maxheap

    def __ismaxparent(self, i):
        left = (i * 2) + 1
        right = (i * 2) + 2
        return left < len(self.heap) - 1 and self.heap[i] > self.heap[left] and \
                right < len(self.heap) and self.heap[i] > self.heap[right]

    def __isminparent(self, i):
        left = (i * 2) + 1
        right = (i * 2) + 2
        return left < len(self.heap) - 1 and self.heap[i] < self.heap[left] and \
               right < len(self.heap) and self.heap[i] < self.heap[right]


numbers = [10, 4, 5, 1, 3, 2]
maxheap = CheckMaxheap(numbers)
print(maxheap.ismaxheap())