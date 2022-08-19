# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def build(nums):
            total = len(nums)
            if not total:
                return None
            mid = len(nums)//2
            
            root = TreeNode(nums[mid])
            root.left = build(nums[:mid])
            root.right = build(nums[mid+1:])
            
            return root
        return build(nums)