# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=None
        self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return None
        self.dfs(node.right)
        self.dfs(node.left)
        node.left=None
        node.right=self.prev
        self.prev=node
        