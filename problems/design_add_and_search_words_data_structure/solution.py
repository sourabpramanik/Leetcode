class Node:
    def __init__(self):
        self.nodes = {}
        self.flag = False
        
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        root = self.root
        
        for c in word:
            if c not in root.nodes:
                root.nodes[c] = Node()
            root = root.nodes[c]
        root.flag = True

    def search(self, word: str) -> bool:
        
        def dfs(root, i):
            if i==len(word):
                return root.flag
            
            ch = word[i]
            
            if ch == ".":
                 for n in root.nodes:
                        if dfs(root.nodes[n], i+1):
                            return True
                        
            if ch in root.nodes:
                return dfs(root.nodes[ch], i+1)
            
            return False
        
        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)