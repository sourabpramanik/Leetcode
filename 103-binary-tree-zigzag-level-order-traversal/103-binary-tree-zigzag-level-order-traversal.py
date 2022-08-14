# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return root
        
        queue = collections.deque([root])
        ans = []
        level = 1
        
        while queue:
            aux = []
            size = len(queue)
            
            for v in range(size):
                node = queue.popleft()
                aux.append(node.val)
                
                if node:
                    node.left and queue.append(node.left)                    
                    node.right and queue.append(node.right)                              
            
            ans.append(aux[::level])
            level *= (-1)
            
        return ans