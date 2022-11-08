# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        counter = 0
        
        if not root:
            return counter
        
        queue = collections.deque([root])
        
        
        while queue:
            for _ in range(len(queue)):                
                node  = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            counter+=1
        
        return counter