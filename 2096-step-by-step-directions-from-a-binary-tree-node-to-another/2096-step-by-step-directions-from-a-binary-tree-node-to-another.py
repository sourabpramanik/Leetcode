# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int,) -> str:        
        
        def lca(node):
            if not node or node.val == sv or node.val == dv:                
                return node
            
            left = lca(node.left)
            right = lca(node.right)
            
            if left and right:
                return node
            return left or right
        
        root = lca(root)
        
        start = dest = ""
        
        stack = [(root, "")]
        
        while stack:
            
            node, path = stack.pop()
            
            if node.val==sv: start = path
            if node.val==dv: dest = path
                
            if node.left:
                stack.append((node.left, path+"L"))
            if node.right:
                stack.append((node.right, path+"R"))
        
        return "U"*len(start)+dest
        
        
                
                