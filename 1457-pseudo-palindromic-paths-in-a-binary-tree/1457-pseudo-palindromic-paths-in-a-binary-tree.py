# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        def rec(node, setI):
            if not node: return 0
            if node.val in setI:
                setI.remove(node.val)
            else:
                setI.add(node.val)
            res=0
            if not node.left and not node.right:
                if len(setI)<=1: res=1
            
            l = rec(node.left, setI)
            r = rec(node.right, setI)
            
            if node.val in setI:
                setI.remove(node.val)
            else:
                setI.add(node.val)
                
            return res+l+r
        
        return rec(root, set())
        
        
      
        
        