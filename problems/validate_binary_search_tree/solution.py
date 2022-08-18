# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node, minVal, maxVal):
            if node is None: return True
            
            if node.val>=maxVal or node.val<=minVal: return False
            
            return valid(node.left, minVal, node.val) and valid(node.right, node.val, maxVal)
        return valid(root, float("-inf"), float("inf"))