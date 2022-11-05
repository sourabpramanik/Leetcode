# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        
        
        stack = []
        prev_node = TreeNode(float("-inf"))
        first_node = None
        last_node = None
        
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                if len(stack):
                    root = stack.pop()
                    if not first_node and root.val < prev_node.val:
                        first_node = prev_node
                    
                    if first_node and root.val  < prev_node.val:
                        last_node = root
                    
                    prev_node = root
                    root = root.right
                
        first_node.val, last_node.val = last_node.val, first_node.val
        