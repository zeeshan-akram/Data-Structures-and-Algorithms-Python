class Stack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if len(self.stack2) == 0:
            for i in range(len(self.stack1)-1, -1, -1):
                self.stack2.append(self.stack1[i])
        try:
            self.stack2.pop(len(self.stack2)-1)
            self.stack1.pop(0)
        except IndexError:
            print('Stack is Empty')

    def isEmpty(self):
        if len(self.stack2) == 0 \
                and len(self.stack1) == 0:
            print(True)
        else:
            print(False)

    def show(self):
        print(self.stack1)


stack = Stack()
stack.enqueue(3)
stack.enqueue(4)
stack.dequeue()
stack.enqueue(5)
stack.dequeue()
stack.show()
stack.isEmpty()