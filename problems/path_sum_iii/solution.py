# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec(self, node, T):
        if node:
            return int(T==node.val) + self.rec(node.left, T-node.val) + self.rec(node.right, T-node.val)       
        
        return 0
    def pathSum(self, root: Optional[TreeNode], T: int) -> int:
        if root:
            return self.rec(root, T) + self.pathSum(root.left, T) + self.pathSum(root.right, T)         
        return 0
    
    
        
        