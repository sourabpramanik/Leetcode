# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.depth = 0
        self.ans = None
        
        def dfs(node, curr):
            self.depth = max(curr, self.depth)
            if node is None:
                return curr
            
            left = dfs(node.left, curr+1)
            right = dfs(node.right, curr+1)
            
            if left==right==self.depth:
                self.ans=node                
                
            return max(left, right)
        dfs(root, 0)
        return self.ans
                