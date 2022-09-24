# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], T: int) -> List[List[int]]:
        if root is None: return []
        
        if root.left is None and root.right is None and T-root.val==0:
            return [[root.val]]
        
        temp = self.pathSum(root.left, T-root.val) + self.pathSum(root.right, T-root.val)
        
        return [[root.val]+i for i in temp]