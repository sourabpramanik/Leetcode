# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 1
        
        lh=self.isBalanced(root.left)
        rh=self.isBalanced(root.right)

        if abs(lh-rh)>1:
            return 0
        if not lh or not rh:
            return 0
        return 1+max(lh, rh)

