# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.arr = []
        
        self.preOrder(root, self.arr)
        
        obj={}
        
        for i in range(0, len(self.arr)):
            rem = k-self.arr[i]
            
            if rem in obj:
                return True
            else:
                obj[self.arr[i]] = 1
        return False
    
    def preOrder(self, node, arr):
        
        if not node:
            return None
        
        arr.append(node.val)
        self.preOrder(node.left, arr)
        self.preOrder(node.right, arr)
    
    