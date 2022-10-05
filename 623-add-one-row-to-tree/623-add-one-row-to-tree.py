# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            n = TreeNode(val)
            n.left = root
            return n
        
        def rec(node, d, n):
            
            if not node:
                return None
            
            if d==n-1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp
                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp
            
            else:
                rec(node.left, d+1, n)
                rec(node.right, d+1, n)
                
        
        rec(root, 1, depth)
        return root
        