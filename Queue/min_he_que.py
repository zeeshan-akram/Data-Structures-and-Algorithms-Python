from min_heap import MinHeap


class MinQueue:
    def __init__(self):
        self.heap = MinHeap()

    def enqueue(self, key, string):
        self.heap.push(key, string)

    def dequeue(self):
        return self.heap.pop()

    def display(self):
        self.heap.show()

    def isEmpty(self):
        return self.heap.isEmpty()


#queue = MinQueue()
#queue.enqueue(int(6), str('Ali'))
#queue.enqueue(int(5), str('Umer'))
#queue.enqueue(int(1), str('ahsan'))
#queue.enqueue(int(7), str('haider'))
#queue.enqueue(int(8), str('moiz'))
#queue.enqueue(int(9), str('umair'))
#queue.enqueue(int(3), str('farrukh'))
#print(queue.dequeue())
#print(queue.dequeue())
#print(queue.dequeue())
#print(queue.isEmpty())