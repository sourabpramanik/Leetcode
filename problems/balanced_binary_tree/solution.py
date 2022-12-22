# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.flag=True
        
        def dfs(node):
            if not node: return 0
            
            l=dfs(node.left)
            r=dfs(node.right)

            if l==-1 or r==-1:
                return -1
            if abs(l-r)>1:
                return -1

            return 1+max(l, r)

        return False if dfs(root)==-1 else True