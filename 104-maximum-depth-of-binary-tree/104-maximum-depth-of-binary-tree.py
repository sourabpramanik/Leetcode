# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        self.large = float('-inf')
        
        def dfs(node, num):
            if not node: return
            
            if not node.left and not node.right:
                self.large = max(self.large, num)
            
            dfs(node.left, num+1)
            dfs(node.right, num+1)
        
        dfs(root, 1)
        
        return self.large