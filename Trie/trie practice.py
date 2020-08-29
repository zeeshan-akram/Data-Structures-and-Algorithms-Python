class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = {}
        self.isEndOfWords = bool

    def insertchild(self, ch):
        self.children[ch] = Node(ch)

    def getchild(self, ch):
        return self.children.get(ch)

    def getchildrens(self):
        return self.children.values()

    def haschildrens(self):
        return len(self.children) != 0

    def isEndofword(self):
        return True if self.isEndOfWords is True else False

    def remove(self, ch):
        self.children.pop(ch)


class Trie:
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.totalwords = 0

    def insert(self, string):
        current = self.root
        for ch in string:
            if ch not in current.children:
                current.insertchild(ch)
            current = current.getchild(ch)
        current.isEndOfWords = True

    def contains(self, word):
        current = self.root
        for ch in word:
            if current.getchild(ch) is None:
                return False
            else:
                current = current.getchild(ch)
        return current.isEndofword()

    def transverse(self):
        self.__transverse(self.root)

    def __transverse(self, root):
        if root.value is not None:
            print(root.value)
        for child in root.getchildrens():
            self.__transverse(child)

    def remove(self, word):
        self.__remove(self.root, word, index=0)

    def __remove(self, root, word, index):
        if index == len(word):
            root.isEndOfWords = False
            return
        ch = word[index]
        child = root.getchild(word[index])
        if child is None:
            return
        self.__remove(child, word, index+1)
        if not root.isEndofword() and not root.haschildrens():
            root.remove(ch)

    def findwords(self, string):
        current = self.root
        for ch in string:
            current = current.getchild(ch)
        words = []
        self.__automate(current, string, words)
        return words

    def __automate(self, root, string, words):
        if root.isEndofword():
            words.append(string)
        for child in root.getchildrens():
            self.__automate(child, string+child.value, words)

    def containsRecursive(self, word):
        return self.__containsRecursive(self.root, word, index=0)

    def __containsRecursive(self, root, word, index):
        if index == len(word):
            return True if root.isEndofword() else False
        ch = word[index]
        if root.getchild(ch) is None:
            return False
        child = root.getchild(ch)
        return self.__containsRecursive(child, word, index+1)

    def countWords(self):
        self.__countWords(self.root)
        print(self.totalwords)

    def __countWords(self, root):
        if root is None:
            return
        for child in root.getchildrens():
            if child.isEndofword():
                self.totalwords += 1
            self.__countWords(child)

    def longestCommonPrefix(self, string):
        common = []
        for word in string:
            com = self.__longestCommonPrefix(self.root, word)
            common.append(com)
        if common.count(com) == len(common):
            print(f'"{com}"')
        else:
            print('""')

    def __longestCommonPrefix(self, root, string):
        word = ''
        for ch in string:
            if root.isEndofword():
                break
            word += ch
            root = root.getchild(ch)
        return word


trie = Trie()
trie.insert('car')
trie.insert('card')
trie.insert('dog')
trie.insert('truth')
trie.insert('careful')
#print(trie.containsRecursive('ca'))
#print(trie.findwords('car'))
trie.countWords()
check = ['car', 'card', 'careful']
trie.longestCommonPrefix(check)
