class Node:
    def __init__(self):
        self.links = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        root = self.root
        for w in word:
            if not w in root.links:
                root.links[w] = Node()
            root = root.links[w]
        
        root.end = True
    
    def getLong(self,word):
        root = self.root
        long = ""
        for w in word:
            if root.links[w].end==False:
                return ""
            root = root.links[w]            
        return word
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        trie = Trie()
        long = ""
        for v in words:
            trie.insert(v)
            
        for v in words:
            if len(long) < len(trie.getLong(v)):
                long = trie.getLong(v)
            elif len(long) == len(trie.getLong(v)):
                if long > trie.getLong(v):
                    long = trie.getLong(v)
        
        return long
        
        