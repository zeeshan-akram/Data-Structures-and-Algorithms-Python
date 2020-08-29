class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node()
        self.last = self.head

    def enqueue(self, data):
        new_node = Node(data)
        self.last.next = new_node
        self.last = new_node

    def dequeue(self):
        current = self.head

        current = current.next
        self.head.next = current.next

    def peek(self):
        current = self.head
        current = current.next
        print(current.data)

    def size(self):
        current = self.head
        count = 0
        while current.next is not None:
            current = current.next
            count += 1
        print(count)

    def isEmpty(self):
        current = self.head
        if current.next is None:
            print(True)
        else:
            print(False)

    def show(self):
        element = []
        current = self.head
        while current.next is not None:
            current = current.next
            element.append(current.data)
        print(element)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.size()
queue.isEmpty()
queue.dequeue()
queue.peek()
queue.size()
queue.show()