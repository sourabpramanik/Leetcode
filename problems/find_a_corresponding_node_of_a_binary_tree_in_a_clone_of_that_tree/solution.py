# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        self.tree = None
        def rec(node):
            
            if not node:
                return None
            
            if node.val == target.val:
                self.tree =  node
            else:
                rec(node.left)
                rec(node.right)
        rec(cloned)
        
        return self.tree 
        
        