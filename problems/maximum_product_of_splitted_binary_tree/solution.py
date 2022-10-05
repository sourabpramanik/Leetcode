# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        val = []
        def rec(node):
            
            if not node:
                return 0
            
            ans = rec(node.left) + rec(node.right) + node.val            
            val.append(ans)
            
            return ans
        
        total = rec(root)
        
        return max((total-x) * x for x in val) % (10**9 + 7)
            