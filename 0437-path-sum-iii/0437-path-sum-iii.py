# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
             
        path = {0:1}
        
        def rec(node, pre_sum):
            if not node:
                return 0
            pre_sum+=node.val
            count = path.get(pre_sum-target, 0)
            path[pre_sum] = path.get(pre_sum, 0) + 1
            count += rec(node.left, pre_sum) + rec(node.right, pre_sum)
            path[pre_sum]-=1

            return count
        
        return rec(root, 0)
                