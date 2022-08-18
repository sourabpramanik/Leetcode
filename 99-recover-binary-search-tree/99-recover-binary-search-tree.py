# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev, first, mid, last = None, None, None, None
    
    def inOrder(self,node):
        if node is None: return None
        
        self.inOrder(node.left)
        
        if(self.prev and node.val < self.prev.val):
            
            if self.first is None:
                self.first = self.prev
                self.mid = node
            
            else:
                self.last = node
        
        self.prev = node
        self.inOrder(node.right)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        self.prev = TreeNode(float("-inf"))
        self.inOrder(root)
        if(self.first and self.last):
            t = self.first.val
            self.first.val = self.last.val
            self.last.val = t
        elif(self.first and self.mid):
            t = self.first.val
            self.first.val = self.mid.val
            self.mid.val = t
        