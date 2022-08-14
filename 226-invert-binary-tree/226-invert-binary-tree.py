# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:        

        
        if root is None: return root
        
        def recur(node):
            if node is None: return None
            newTree = TreeNode(node.val)
            newTree.left = recur(node.right)
            newTree.right = recur(node.left)
            
            return newTree
        
        
        
        return recur(root)
        