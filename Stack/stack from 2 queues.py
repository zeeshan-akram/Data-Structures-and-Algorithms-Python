class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        push = self.check()
        push.append(data)

    def pop(self):
        pop = self.shifting()
        pop.pop(0)

    def peek(self):
        peek = self.check()
        print(peek[0])

    def isEmpty(self):
        empty = self.check()
        if len(empty) == 0:
            print(True)
        else:
            print(False)

    def show(self):
        print(self.check())

    def shifting(self):
        if len(self.queue2) == 0:
            for i in range(len(self.queue1)-1):
                self.queue2.append(self.queue1.pop(i))
            return self.queue1
        else:
            for i in range(len(self.queue2)-1):
                self.queue1.append(self.queue2.pop(i))
            return self.queue2

    def check(self):
        if len(self.queue2) == 0:
            return self.queue1
        else:
            return self.queue2


stack = Stack()
stack.push(1)
stack.push(2)
stack.pop()
stack.push(3)
stack.show()
stack.peek()
stack.isEmpty()