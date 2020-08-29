class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def reversed(self, k):
        first = 0
        last = k-1
        while first!=last and first<last:
            temp = self.queue[first]
            self.queue[first] = self.queue[last]
            self.queue[last] = temp
            first += 1
            last -= 1
        print(self.queue)

que = Queue()
que.enqueue(10)
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)
que.enqueue(60)
que.enqueue(70)
que.reversed(4)