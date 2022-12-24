# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float("-inf")
        self.dfs(root)
        return self.maxi
    
    def dfs(self, node):
        if not node:
            return 0
        
        l=max(0, self.dfs(node.left))
        r=max(0, self.dfs(node.right))
        self.maxi=max(self.maxi, node.val+l+r)
        return node.val+max(l, r)
