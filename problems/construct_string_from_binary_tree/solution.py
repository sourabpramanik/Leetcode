# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        res = str(root.val)
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        strL = str(left)
        strR = str(right)
        
        if(strL=="" and strR==""): return res
        if(strL==""): return res + "()" + "(" + strR + ")"
        if(strR==""): return res + "(" + strL + ")"        
            
        return  res + "(" + strL + ")" + "(" + strR + ")"