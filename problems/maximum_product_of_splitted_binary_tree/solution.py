# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        total=0
        vals=[]
        def dfs(node):
            if not node:
                return 0

            l=dfs(node.left)
            r=dfs(node.right)            

            self.ans=max(self.ans, l*(total-l), r*(total-r))            
            return node.val+l+r
        
        total=dfs(root)
        dfs(root)
        return self.ans % ((10**9)+7)
