class Queue:
    def __init__(self):
        self.queue = [0, 0, 0, 0, 0, 0]
        self.rear = 0
        self.front = 0
        self.count = 0

    def enqueue(self, data):
        if len(self.queue) == self.count:
            print('Queue is full')
        else:
            self.queue[self.rear] = data
            self.rear = (self.rear + 1) % 6   #circular queue
            self.count += 1

    def dequeue(self):
        if self.count == 0:
            print('Queue is empty')
        else:
            self.queue[self.front] = 0
            self.front = (self.front + 1) % 6    #circular queue
            self.count -= 1

    def isFull(self):
        if len(self.queue)==self.count:
            return True
        else:
            return False

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def reverse(self):
        first = 0
        last = len(self.queue) - 1
        while first != last and first < last:
            temp = self.queue[first]
            self.queue[first] = self.queue[last]
            self.queue[last] = temp
            first += 1
            last -= 1
        return self.queue

    def show(self):
        print(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.show()