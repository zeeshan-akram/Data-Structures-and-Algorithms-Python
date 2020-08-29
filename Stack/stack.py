class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        try:
            le = len(self.stack)
            pop = self.stack.pop(le-1)
            return pop
        except IndexError:
            print('Stack is empty')

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        if len(self.stack) == 0:
            print('Stack is Empty')
        else:
            ind = len(self.stack) - 1
            print(self.stack[ind])

    def show(self):
        print(self.stack)

def balance(mystr):
    stack = Stack()
    index = 0
    result = ''
    open = ['[', '{', '(', '<']
    close = [']', '}', ')', '>']
    for ch in mystr:
        if ch in open:
            stack.push(ch)
            index += 1
        elif ch in close:
            check = stack.pop()
            if close.index(ch) == open.index(check):
                result = 'Balanced'
            else:
                result = 'Unbalanced'
                break
            index -= 1
        elif index == 0:
            result = 'Balance'
        else:
            result = 'Unbalanced'
    print(result)


string = 'zeeshan'
reverse = ''
stack = Stack()
stack.push(1)
stack.push(2)
stack.show()
stack.peek()
print(stack.isEmpty())
stack.pop()
stack.pop()