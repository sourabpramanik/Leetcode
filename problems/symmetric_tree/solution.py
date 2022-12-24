# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 or not node2:
                return node1==node2
            
            if node1.val!=node2.val:
                return False
            
            l = dfs(node1.left, node2.right)
            r = dfs(node1.right, node2.left)

            if l and r:
                return True
            return False
        return dfs(root.left, root.right)