# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def rec(node):
            if node:
                if node.left and not node.left.left and not node.left.right:
                    self.sum+=node.left.val
                rec(node.left)
                rec(node.right)
        rec(root)
        return self.sum
        