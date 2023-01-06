# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, node1, node2):
        if not node1 or not node2:
            return node1==node2
        
        if node1.val!=node2.val:
            return False
        l=self.dfs(node1.left, node2.right)
        r=self.dfs(node1.right, node2.left)

        if not l or not r:
            return False
        return True