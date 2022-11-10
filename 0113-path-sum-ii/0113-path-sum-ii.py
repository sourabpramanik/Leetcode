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
        queue = [(root, root.val, [root.val])]
        
        while queue:
            node, val, ds = queue.pop(0)
            if not node.left and not node.right and val == targetSum:
                res.append(ds)
            
            if node.left:
                queue.append((node.left, val+node.left.val, ds+[node.left.val]))
            if node.right:
                queue.append((node.right, val+node.right.val, ds+[node.right.val]))
            
        return res