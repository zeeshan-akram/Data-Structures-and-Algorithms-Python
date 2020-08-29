class Priorityqueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        l = len(self.queue)
        if l == 0 or data > self.queue[l-1]:
            self.queue.append(data)
        else:
            for i in range(len(self.queue)):
                if data < self.queue[i]:
                    self.queue.insert(i, data)
                    break

    def dequeue(self):
        self.queue.pop(0)

    def show(self):
        print(self.queue)


queue = Priorityqueue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(2)
queue.enqueue(1)
queue.show()
