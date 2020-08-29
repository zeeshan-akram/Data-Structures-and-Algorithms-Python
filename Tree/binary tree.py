from itertools import zip_longest
INT_MAX = 4294967296
INT_MIN = -4294967296

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = Node()

    def insert(self, value):
        if self.root.value is None:
            self.root.value = value
        else:
            current = self.root
            new_child = Node(value)
            while True:
                if value > current.value:
                    if current.right is None:
                        break
                    else:
                        current = current.right
                else:
                    if current.left is None:
                        break
                    else:
                        current = current.left
            if value > current.value:
                current.right = new_child
            else:
                current.left = new_child

    def height(self):
        return self.findheight(self.root)

    def findheight(self, root):

        if root.right is not None and root.left is not None:
            return 1 + max(self.findheight(root.left), self.findheight(root.right))
        elif root.left is None and root.right is not None:
            return 1 + self.findheight(root.right)
        elif root.left is not None and root.right is None:
            return 1 + self.findheight(root.left)
        else:
            return 0

    def preorder(self):
        self.pretransverse(self.root)

    def pretransverse(self, root):
        if root.right is not None and root.left is not None:
            print(root.value)
            self.pretransverse(root.left)
            self.pretransverse(root.right)
        elif root.left is None and root.right is not None:
            print(root.value)
            self.pretransverse(root.right)
        elif root.left is not None and root.right is None:
            print(root.value)
            self.pretransverse(root.left)
        else:
            print(root.value)
            return

    def inorder(self):
        self.intransverse(self.root)

    def intransverse(self, root):
        if root.right is not None and root.left is not None:
            self.intransverse(root.left)
            print(root.value)
            self.intransverse(root.right)
        elif root.left is None and root.right is not None:
            print(root.value)
            self.intransverse(root.right)
        elif root.left is not None and root.right is None:
            self.intransverse(root.left)
            print(root.value)
        else:
            print(root.value)
            return

    def postorder(self):
        self.posttransvers(self.root)

    def posttransvers(self, root):
        if root.right is not None and root.left is not None:
            self.posttransvers(root.left)
            self.posttransvers(root.right)
            print(root.value)
        elif root.left is None and root.right is not None:
            self.posttransvers(root.right)
            print(root.value)
        elif root.left is not None and root.right is None:
            self.posttransvers(root.left)
            print(root.value)
        else:
            print(root.value)
            return

    def min(self):
        result = self.minfind(self.root)
        print(result)

    def minfind(self, root):
        if root.right is not None and root.left is not None:
            return min(min(self.minfind(root.left), self.minfind(root.right)), root.value)
        elif root.left is None and root.right is not None:
            return min(root.value, self.minfind(root.right))
        elif root.left is not None and root.right is None:
            return min(root.value, self.minfind(root.left))
        else:
            return root.value

    def find(self, value):
        current = self.root
        while True:
            if current.value == value:
                print(True)
                break
            if value > current.value:
                if current.right is None:
                    print(False)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    print(False)
                    break
                else:
                    current = current.left

    def isbinary(self):
        return self.equal(self.root, INT_MIN, INT_MAX)

    def equal(self, root, min, max):
        if root.right is not None and root.left is not None:
            if min > root.value > max:
                return False
            return self.equal(root.left, min, max=root.value - 1) and \
                   self.equal(root.right, root.value + 1, max)
        elif root.left is None and root.right is not None:
            if min > root.value > max:
                return False
            return self.equal(root.right, root.value + 1, max)
        elif root.left is not None and root.right is None:
            if min > root.value > max:
                return False
            return self.equal(root.left, min, max=root.value - 1)
        else:
            return True

    def distance(self, dist):
        list = []
        self.finddistance(self.root, dist, list)
        return list

    def finddistance(self, root, dist, list):
        if root.right is not None and root.left is not None:
            if dist == 0:
                list.append(root.value)
                return
            else:
                dist -= 1
                self.finddistance(root.left, dist, list)
                self.finddistance(root.right, dist, list)
        elif root.left is None and root.right is not None:
            if dist == 0:
                list.append(root.value)
                return
            else:
                dist -= 1
                self.finddistance(root.right, dist, list)
        elif root.left is not None and root.right is None:
            if dist == 0:
                list.append(root.value)
                return
            else:
                dist -= 1
                self.finddistance(root.left, dist, list)
        else:
            if dist == 0:
                list.append(root.value)
                return
            return

    def levelorder(self):
        self.leveltransverse()

    def leveltransverse(self):
        for i in range(self.height()+1):
            value = self.distance(i)
            for val in value:
                print(val)


tree1 = Tree()
tree1.insert(10)
tree1.insert(5)
tree1.insert(15)
tree1.insert(6)
tree1.insert(1)
tree1.insert(8)
tree1.insert(12)
tree1.insert(18)
tree1.insert(17)
tree1.preorder()
print(tree1.isbinary())
print(tree1.distance(3))
tree1.levelorder()
