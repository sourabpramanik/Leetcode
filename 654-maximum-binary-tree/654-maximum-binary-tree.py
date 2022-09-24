# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.build(nums)
    
    def build(self, a):
        if not a:
            return
        
        maxV = max(a)
        maxI  = a.index(maxV)
        
        tree = TreeNode(maxV)
        tree.left = self.build(a[:maxI])        
        tree.right = self.build(a[maxI+1:])
        
        return tree