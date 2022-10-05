# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        
        stack = []
        stack.append(root)
        
        while len(stack)!=0:
            
            node = stack.pop()
            
            if low <= node.val <= high:
                self.sum += node.val
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        
        
        return self.sum