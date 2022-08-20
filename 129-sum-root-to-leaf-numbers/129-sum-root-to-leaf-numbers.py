# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return None
        
        res = []       
        sum = 0
        
        def rec(node, ls):
            if node is None: return res
            
            if not node.left and not node.right:
                res.append(ls+str(node.val))
                
            if node.right:
                rec(node.right, ls+str(node.val))
            if node.left:
                rec(node.left, ls+str(node.val))
        
        rec(root, "")
            
        for v in res:
            sum += int(v)
        
        return sum