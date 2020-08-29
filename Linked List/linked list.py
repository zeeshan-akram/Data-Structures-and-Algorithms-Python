class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.last = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.last = new_node

    def addFirst(self, data):
        new_node = Node(data)
        current = self.head
        second = current.next
        new_node.next = second
        current.next = new_node

    def addLast(self, data):
        new_node = Node(data)
        if self.last.data is None:
            current = self.head
            current.next = new_node
        else:
            last = self.last
            last.next = new_node
        self.last = new_node

    def deleteFirst(self):
        current = self.head
        first = current.next
        second = first.next
        current.next = second

    def deleteLast(self):
        current = self.head
        record = self.head
        while current.next is not None:
            current = current.next
            if current.next is not None:
                record = current
        record.next = current.next

    def index(self, data):
        current = self.head
        idx = -1
        try:
            while current.data != data:
                current = current.next
                idx += 1
            print(idx)
        except AttributeError:
            print('Not Found')

    def length(self):
        current = self.head
        len = 0
        while current.next is not None:
            current = current.next
            len += 1
        return len

    def contain(self, data):
        current = self.head
        try:
            while current.data != data:
                current = current.next
                if current.data == data:
                    print("Yes List have it")
        except AttributeError:
            print("List don't have")

    def findMiddle(self):
        le = self.length()
        current = self.head
        middle = self.head
        for i in range(le//2):
            current = current.next
        while current.next is not None:
            current = current.next
            middle = middle.next
        if le%2 == 0:
            middle1 = middle.next
            print(middle.data, middle1.data)
        else:
            print(middle.data)

    def reverse(self):
        current = self.head
        transverse = self.head
        new = current.next
        new = new.next
        current = current.next
        transverse.next = None
        while current.next is not None:
            current.next = transverse
            transverse = current
            current = new
            if new.next is not None:
                new = new.next
        current.next = transverse
        show = current
        ele = []
        while show.next is not None:
            if show.next is not None:
                ele.append(show.data)
            show = show.next
        print(ele)

    def checkLoop(self):
        slow = self.head
        fast = self.head
        while fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
            slow = slow.next
            if slow == fast:
                result = 'Loop found'
            else:
                result = 'Loop not found'
        print(result)


    def convertArray(self):
        current = self.head
        array = []
        while current.next is not None:
            current = current.next
            array.append(current.data)
        return array

    def getKthFromEnd(self, data):
        current = self.head
        start = self.head
        if data < 1:
            print('Wrong Index')
        else:
            try:
                n = data - 1
                for i in range(n):
                    current = current.next
                while current.next is not None:
                    current = current.next
                    start = start.next
                print(start.data)
            except AttributeError:
                print("Larger value")


    def display(self):
        elements = []
        current = self.head
        while current.next is not None:
            current = current.next
            elements.append(current.data)
        print(elements)


li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.addFirst(0)
li.addLast(4)
li.addLast(5)
li.addLast(6)
li.display()
li.getKthFromEnd(5)
li.findMiddle()
li.checkLoop()