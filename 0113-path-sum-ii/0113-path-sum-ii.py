# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        stack = [(root, targetSum-root.val, [root.val])]
        
        while stack:
            node, target, ds = stack.pop()
            if not node.left and not node.right and target==0:
                res.append(ds)
            
            if node.left:
                stack.append((node.left, target-node.left.val, ds+[node.left.val]))
            if node.right:
                stack.append((node.right, target-node.right.val, ds+[node.right.val]))
            
        return res