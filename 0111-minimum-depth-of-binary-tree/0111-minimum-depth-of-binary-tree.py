# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.h=float("inf")
        def dfs(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                self.h = min(self.h, depth)
            lh = dfs(node.left, depth+1)
            rh = dfs(node.right, depth+1)
        dfs(root, 1)
        return 0 if self.h==float("inf") else self.h