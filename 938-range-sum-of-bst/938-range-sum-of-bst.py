# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        
        def rec(node):
            if not node:
                return 0
            
            if low <= node.val <= high:
                self.sum += node.val
                
            rec(node.left)
            rec(node.right)
        
        rec(root)
        
        return self.sum