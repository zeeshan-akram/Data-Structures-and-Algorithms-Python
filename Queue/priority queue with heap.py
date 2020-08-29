from heap_optimize import Heap
class PriorityQueue:
    def __init__(self):
        super().__init__()
        self.heap = Heap()

    def enqueue(self, value):
        self.heap.push(value)

    def dequeue(self):
        print(self.heap.pop())

    def showQueue(self):
        print(self.heap.heap)


queue = PriorityQueue()
queue.enqueue(10)
queue.enqueue(8)
queue.enqueue(4)
queue.enqueue(2)
queue.dequeue()
queue.dequeue()
queue.showQueue()