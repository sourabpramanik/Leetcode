class Node:
    def __init__(self):
        self.nodes = {}
        self.flag = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        
        for w in word:
            if w not in root.nodes:
                root.nodes[w] = Node()
            root = root.nodes[w]
        root.flag = True

    def search(self, word: str) -> bool:
        root = self.root
        
        for w in word:
            if w not in root.nodes:
                return False
            root = root.nodes[w]
        
        return root.flag

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        
        for w in prefix:
            if w not in root.nodes:
                return False
            root = root.nodes[w]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)