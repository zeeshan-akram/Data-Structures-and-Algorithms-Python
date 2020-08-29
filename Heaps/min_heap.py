class MinHeap:
    def __init__(self):
        super().__init__()
        self.minHeap = []

    def push(self, key, string):
        self.minHeap.append((key, string))
        self.__bubbleup(len(self.minHeap) - 1)

    def pop(self):
        removed = self.minHeap[0]
        if len(self.minHeap) > 1:
            self.minHeap[0] = self.minHeap.pop()
            self.__bubbledown(0)
        elif len(self.minHeap) == 1:
            self.minHeap.pop()
        return removed

    def __bubbledown(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        smallest = index
        parent_key = self.minHeap[index]
        if left <= len(self.minHeap) - 1 and self.__leftKey(parent_key, left, right):
            smallest = left
        if right < len(self.minHeap) - 1 and self.__rightKey(parent_key, right):
            smallest = right
        if smallest != index:
            self.__swap(smallest, index)
            self.__bubbledown(index)

    def __rightKey(self, parent_key, right):
        if right < len(self.minHeap) - 1:
            right_key = self.minHeap[right]
            if parent_key[0] > right_key[0]:
                return True
            else:
                return False
        else:
            return False

    def __leftKey(self, parent_key, left, right):
        if left <= len(self.minHeap) - 1 and right < len(self.minHeap) - 1:
            left_key = self.minHeap[left]
            right_key = self.minHeap[right]
            if parent_key[0] > left_key[0] < right_key[0]:
                return True
            else:
                return False
        elif left <= len(self.minHeap) - 1:
            left_key = self.minHeap[left]
            if parent_key[0] > left_key[0]:
                return True
            else:
                return False
        else:
            return False

    def __bubbleup(self, index):
        if index <= 0:
            return
        parent = (index - 1) // 2
        child_key = self.minHeap[index]
        parent_key = self.minHeap[parent]
        if child_key[0] < parent_key[0]:
            self.__swap(parent, index)
            self.__bubbleup(parent)

    def isEmpty(self):
        return len(self.minHeap) == 0

    def __swap(self, parent, child):
        self.minHeap[parent], self.minHeap[child] = self.minHeap[child], self.minHeap[parent]

    def show(self):
        print(self.minHeap)

# minheap = MinHeap()
# minheap.push(int(6), str('Ali'))
# minheap.push(int(5), str('Umer'))
# minheap.push(int(1), str('ahsan'))
# minheap.push(int(7), str('haider'))
# minheap.push(int(8), str('moiz'))
# minheap.push(int(9), str('umair'))
# minheap.push(int(3), str('farrukh'))
# minheap.show()
# minheap.pop()
# minheap.show()
