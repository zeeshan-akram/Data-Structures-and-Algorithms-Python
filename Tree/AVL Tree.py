class Node:
    def __init__(self, data=None):
        self.height = 0
        self.data = data
        self.left = None
        self.right = None


class AvlTree:
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
        else:
            self.root = self.inserting(self.root, data)


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

    def inserting(self, root, data):
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self.inserting(root.right, data)
        elif data < root.data:
            root.left = self.inserting(root.left, data)

        self.setheight(root)
        root = self.rotate(root)
        return root

    def rotate(self, root):
        self.balanceFactor(root)
        if self.isleftheavy(root):
            if self.balanceFactor(root.left) < 0:
                root.left = self.leftrotate(root.left)
            return self.leftrotate(root)

        elif self.isrightheavy(root):
            if self.balanceFactor(root.right) > 0:
                root.right = self.leftrotate(root.right)
            return self.leftrotate(root)
        return root

    def leftrotate(self, root):
        newroot = root.right
        root.right = newroot.left
        newroot.left = root
        self.setheight(root)
        self.setheight(newroot)
        return newroot

    def rightrotate(self, root):
        newroot = root.left
        root.left = newroot.right
        newroot.right = root
        self.findheight(root)
        self.findheight(newroot)
        return newroot

    def setheight(self, root):
        root.height = max(self.findheight(root.left),
                          self.findheight(root.right)) + 1

    def isleftheavy(self, root):
        return self.balanceFactor(root) > 1

    def isrightheavy(self, root):
        return self.balanceFactor(root) < -1

    def balanceFactor(self, root):
        if root is None:
            return 0
        else:
            return self.findheight(root.left) - self.findheight(root.right)

    def findheight(self, root):
        if root is None:
            return -1
        else:
            return root.height


tree = AvlTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)