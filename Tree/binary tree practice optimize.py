Min = -1000000000
Max = 1000000000
class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        self.root = Node(None)

    def insert(self, value):
        node = Node(value)
        if self.root.value is None:
            self.root = node
        else:
            current = self.root
            while True:
                if value > current.value:
                    if current.right is None:
                        current.right = node
                        break
                    else:
                        current = current.right
                elif value < current.value:
                    if current.left is None:
                        current.left = node
                        break
                    else:
                        current = current.left

    def find(self, value):
        current = self.root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
        return False

    def preorder(self):
        self.pretransvers(self.root)

    def pretransvers(self, root):
        if root is None:
            return
        print(root.value)
        self.pretransvers(root.left)
        self.pretransvers(root.right)

    def inorder(self):
        self.intransvers(self.root)

    def intransvers(self, root):
        if root is None:
            return
        self.intransvers(root.left)
        print(root.value)
        self.intransvers(root.right)

    def postorder(self):
        self.posttransvers(self.root)

    def posttransvers(self, root):
        if root is None:
            return
        self.posttransvers(root.left)
        self.posttransvers(root.right)
        print(root.value)

    def height(self):
        height = self.calculateheight(self.root)
        return height

    def calculateheight(self, root):
        if root is None:
            return -1
        return max(1 + self.calculateheight(root.left), 1 + self.calculateheight(root.right))

    def isbinarytree(self):
        return self.binarychecking(self.root, Min, Max)

    def binarychecking(self, root, min, max):
        if root is None:
            return True
        if min > root.value > max:
            return False
        return self.binarychecking(root.left, min, max=root.value) and \
               self.binarychecking(root.right, root.value, max)

    def k_distance(self, k):
        list = []
        self.finddistance(self.root, k, list)
        return list

    def finddistance(self, root, k, list):
        if root is None:
            return
        if k == 0:
            list.append(root.value)
        k -= 1
        self.finddistance(root.left, k, list)
        self.finddistance(root.right, k, list)

    def transversorder(self):
        for level in range(self.height() + 1):
            for node in self.k_distance(level):
                print(node)

    def size(self):
        return self.findsize(self.root)

    def findsize(self, root):
        if root is None:
            return -1
        return (1 + self.findsize(root.left)) + (1 + self.findsize(root.right))

    def countleafs(self):
        return self.findingleaf(self.root)

    def findingleaf(self, root):
        if root is None:
            return 0
        if root.right is None and root.left is None:
            return 1
        return self.findingleaf(root.left) + self.findingleaf(root.right)

    def maximum(self):
        return self.findingmax(self.root)

    def findingmax(self, root):
        if root.right is None:
            return root.value
        return self.findingmax(root.right)

    def contain(self, data):
        return self.checking(self.root, data)

    def checking(self, root, data):
        if root is None:
            return False
        if data == root.value:
            return True
        if data > root.value:
            return self.checking(root.right, data)
        elif data < root.value:
            return self.checking(root.left, data)

    def ancestors(self):
        list = []
        self.findingancestors(self.root, list)
        print(list)

    def findingancestors(self, root, list):
        if root is None:
            return
        if root.left is not None or root.right is not None:
            list.append(root.value)
        self.findingancestors(root.left, list)
        self.findingancestors(root.right, list)

    def aresiblings(self, s1, s2):
        return self.checksiblings(self.root, s1, s2)

    def checksiblings(self, root, s1, s2):
        for level in range(self.height() + 1):
            if s1 and s2 in self.k_distance(level):
                return True
            else:
                return False



tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(6)
tree.insert(1)
tree.insert(8)
tree.insert(12)
tree.insert(18)
tree.insert(17)
print(tree.find(5))
tree.preorder()
tree.inorder()
tree.postorder()
tree.height()
print(tree.isbinarytree())
print(tree.k_distance(2))
tree.transversorder()
print(f'Size of tree is {tree.size()}' )
print(tree.countleafs())
print(tree.maximum())
print(tree.contain(1))
tree.ancestors()
print(tree.aresiblings(1, 6))