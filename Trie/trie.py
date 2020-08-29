class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.isEndOfWorld = bool

    def haschild(self, ch):
        return self.children.get(ch)

    def insertchild(self, ch):
        self.children[ch] = Node(ch)

    def getchild(self, ch):
        return self.children.get(ch)

    def getChildren(self):
        return self.children.values()

    def removechild(self, ch):
        self.children.pop(ch)

    def isEmpty(self):
        return self.children

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        current = self.root
        for ch in string:
            if not current.haschild(ch):
                current.insertchild(ch)
            current = current.getchild(ch)
        current.isEndOfWorld = True

    def contains(self, string):
        try:
            current = self.root
            for ch in string:
                if not current.haschild(ch):
                    return False
                current = current.getchild(ch)
            if current.isEndOfWorld is True:
                return True
            else:
                return False
        except TypeError:
            print('Wrong Input')

    def transvers(self):
        self.__transverstrie(self.root)

    def __transverstrie(self, root):
        for value in root.getChildren():
            self.__transverstrie(value)
        print(root.value)

    def delete(self, word):
        if word is None:
            return
        self.__delete(self.root, word, index=0)

    def __delete(self, root, word, index):
        if index == len(word):
            root.isEndOfWorld = False
            return
        ch = word[index]
        child = root.getchild(ch)
        if child is None:
            return
        self.__delete(child, word, index + 1)
        if len(child.getChildren()) == 0 and not child.isEndOfWorld:
            root.removechild(ch)

    def findwords(self, string):
        if string is None:
            return
        last_node = self.__findLastNode(string)
        words = []
        self.__AutoCompletion(last_node, string, words)
        return words

    def __findLastNode(self, string):
        current = self.root
        for ch in string:
            child = current.getchild(ch)
            if child is None:
                return None
            current = child
        return current

    def __AutoCompletion(self, root, string, words):
        if root.isEndOfWorld is True:
            words.append(string)
        for child in root.getChildren():
            self.__AutoCompletion(child, string + child.value, words)


trie = Trie()
trie.insert('car')
trie.insert('card')
trie.insert('careful')
print(trie.findwords('c'))