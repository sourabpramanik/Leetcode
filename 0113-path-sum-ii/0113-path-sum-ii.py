# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    def dfs(self, node, target, ds, res):
        if node:
            if not node.right and not node.left and node.val == target:
                ds.append(node.val)
                res.append(ds)
            
            self.dfs(node.left, target-node.val, ds+[node.val], res)
            self.dfs(node.right, target-node.val, ds+[node.val], res)
            