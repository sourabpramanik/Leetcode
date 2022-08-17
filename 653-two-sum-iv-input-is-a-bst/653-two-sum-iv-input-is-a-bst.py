# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BstIterator:
    def __init__(self, root, isRev):
        self.root = root
        self.rev = isRev
        self.stack = list()
        self.pushNode(root)
    
    def next(self):
        node = self.stack.pop()
        if self.rev:
            self.pushNode(node.left)
        else:
            self.pushNode(node.right)
        return node.val
    
    def pushNode(self, node):
        while node:
            self.stack.append(node)
            if self.rev:
                node = node.right
            else: 
                node = node.left
        
    
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None: return False
        
        l = BstIterator(root, False)        
        r = BstIterator(root, True)
        
        i = l.next()        
        j = r.next()
        
        while(i<j):
            if(i+j<k):
                i = l.next()
            elif(i+j>k):
                j = r.next()
            else:
                return True
        
        return False