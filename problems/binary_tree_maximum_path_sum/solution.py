# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=float("-inf")
        self.dfs(root)
        return self.max
    def dfs(self,node):
        if not node:
            return 0
        
        lmax=max(0, self.dfs(node.left))
        rmax=max(0, self.dfs(node.right))

        self.max = max(self.max, node.val+lmax+rmax)

        return node.val+max(lmax, rmax)