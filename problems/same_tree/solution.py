# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(n1, n2):
            if not n1 or not n2:
                return n1==n2
            
            if n1.val != n2.val:
                return False
            
            l=dfs(n1.left, n2.left)
            r=dfs(n1.right, n2.right)

            if l and r:
                return True
            return False

        return dfs(p, q)
            

        