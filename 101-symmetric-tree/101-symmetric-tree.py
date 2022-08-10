# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if (not p and not q):
            return True
        if(p and q and p.val==q.val):
            return self.rec(p.left,q.right) and self.rec(p.right,q.left)
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
       
        return self.rec(root, root)
    
    