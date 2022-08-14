# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def rec(node):
            nonlocal maxVal
            if not node: return 0
            
            leftSum = max(0, rec(node.left))
            rightSum = max(0, rec(node.right))
            
            maxVal = max(maxVal, leftSum+rightSum+node.val)
            
            return max(leftSum, rightSum) + node.val
        
        maxVal = float("-inf")
        rec(root)
        
        return maxVal
        
    
        return temp+root.val