# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def findHeight(node):
            if not node:
                return 0
            
            l=findHeight(node.left)
            r=findHeight(node.right)
            return 1+max(l,r)

        def dfs(node):
            if not node:
                return
            
            lh=findHeight(node.left)
            rh=findHeight(node.right)
            self.dia=max(self.dia, lh+rh)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.dia