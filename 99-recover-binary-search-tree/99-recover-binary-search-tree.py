# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev, first, last = None, None, None
    
    def inOrder(self,node):
        if node is None: return None
        
        self.inOrder(node.left)
        
        if(self.first is None and node.val < self.prev.val):
            self.first = self.prev                
        
        if(self.first and node.val < self.prev.val):
            self.last = node
                
        
        self.prev = node
        self.inOrder(node.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        self.prev = TreeNode(float("-inf"))
        self.inOrder(root)
        
        t = self.first.val
        self.first.val = self.last.val
        self.last.val = t
        