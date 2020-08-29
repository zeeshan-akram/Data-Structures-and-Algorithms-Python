class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node()
        self.last = Node()

    def push(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.last = new_node

    def pop(self):
        try:
            current = self.head
            check = self.head
            current = current.next
            while current.next is not None:
                current = current.next
                check = check.next
            check.next = None
            self.last = check
        except AttributeError:
            print('Stack is empty')

    def isEmpty(self):
        current = self.head
        if current.next is None:
            print(True)
        else:
            print(False)

    def peek(self):
        print(self.last.data)

    def show(self):
        ele = []
        current = self.head
        while current.next is not None:
            current = current.next
            ele.append(current.data)
        print(ele)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.pop()
stack.push(1)
stack.show()
stack.peek()
stack.isEmpty()