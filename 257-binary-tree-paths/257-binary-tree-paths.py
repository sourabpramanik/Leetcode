# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
      
        
        def rec(node, ls):
            if node is None:
                return res
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            rec(node.left, ls+str(node.val)+"->")
            rec(node.right, ls+str(node.val)+"->")
                
        
        rec(root, "")
        
        return res
            