# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.builder(nums, 0, len(nums)-1)
    
    def builder(self, arr, l, r):
        if l>r:
            return None
        
        mid=(l+r)//2
        root=TreeNode(arr[mid])
        root.left=self.builder(arr, l, mid-1)
        root.right=self.builder(arr, mid+1, r)

        return root