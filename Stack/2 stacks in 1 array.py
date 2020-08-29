class Stack:
    def __init__(self):
        self.stack = []
        self.idx1 = -2
        self.idx2 = -1

    def push1(self, data):
        self.stack.append(data)
        self.idx1 += 2

    def push2(self, data):
        self.stack.append(data)
        self.idx2 += 2

    def pop1(self):
        if self.idx1 >= 0:
            self.stack.pop(self.idx1)
            self.idx1 -= 2
            self.idx2 -= 1
        else:
            print('Stack 1 is empty')

    def pop2(self):
        if self.idx2 >= 0:
            self.stack.pop((self.idx2))
            self.idx2 -= 1
        else:
            print('Stack 2 is empty')

    def isEmpty1(self):
        if self.idx1 < 0:
            print(True)
        else:
            print(False)

    def isEmpty2(self):
        if self.idx2 < 0:
            print(True)
        else:
            print(False)

    def show(self):
        print(self.stack)


stack = Stack()
stack.push1(1)
stack.push2(2)
stack.push1(3)
stack.push2(4)
stack.pop1()
stack.pop2()
stack.isEmpty1()
stack.isEmpty2()
stack.show()