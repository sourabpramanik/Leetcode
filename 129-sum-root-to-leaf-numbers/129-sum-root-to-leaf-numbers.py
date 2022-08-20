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
        stack = [(root, "")]
        sum = 0
        while stack:
            node,ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
                
            if node.right:
                stack.append((node.right, ls+str(node.val)))
            if node.left:
                stack.append((node.left, ls+str(node.val)))
            
        for v in res:
            sum += int(v)
        
        return sum