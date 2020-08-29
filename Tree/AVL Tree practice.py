class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0


class AvlTree:
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
        else:
            self.root = self.insertion(self.root, data)

    def find(self, value):
        current = self.root
        while current is not None:
            if value > current.data:
                current = current.right
            elif value < current.data:
                current = current.left
            else:
                return True, current.height
        return False

    def insertion(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.insertion(root.right, data)
        elif data < root.data:
            root.left = self.insertion(root.left, data)
        self.setheight(root)
        root = self.rotation(root)
        return root

    def rotation(self, root):
        if self.isleftheavy(root):
            if self.balancefactor(root.left) < 0:
                root.left = self.leftrotate(root.left)
            return self.rightrotate(root)
        elif self.isrightheavy(root):
            if self.balancefactor(root.right) > 0:
                root.right = self.rightrotate(root.right)
            return self.leftrotate(root)
        return root

    def leftrotate(self, root):
        newnode = root.right
        root.right = newnode.left
        newnode.left = root
        self.setheight(root)
        self.setheight(newnode)
        return newnode

    def rightrotate(self, root):
        newnode = root.left
        root.left = newnode.right
        newnode.right = root
        self.setheight(root)
        self.setheight(newnode)
        return newnode

    def isleftheavy(self, root):
        if self.findheight(root.right) - self.findheight(root.left) < -1:
            return True

    def isrightheavy(self, root):
        if self.findheight(root.right) - self.findheight(root.left) > 1:
            return True

    def setheight(self, root):
        root.height = max(self.findheight(root.left),
                          self.findheight(root.right)) + 1

    def balancefactor(self, root):
        if root is None:
            return 0
        else:
            return self.findheight(root.left) - self.findheight(root.right)

    def findheight(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def balanced(self):
        if not self.isleftheavy(self.root) and \
                not self.isrightheavy(self.root):
            print('tree is balanced')

    def isperfectbinary(self):
        return self.checkbinary(self.root)

    def checkbinary(self, root) -> bool:
        if root is None:
            return False
        if self.findheight(root.left) + 1 == self.findheight(root.right) + 1:
            return True
        if self.checkbinary(root.left) == self.checkbinary(root.right):
            return True
        else:
            return False




avltree = AvlTree()
avltree.insert(10)
avltree.insert(30)
avltree.insert(20)
print(avltree.find(30))
print(avltree.isperfectbinary())
avltree.balanced()