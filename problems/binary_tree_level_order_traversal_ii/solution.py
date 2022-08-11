# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []
        
        queue = deque([root])
        ans = []
        
        while queue:
            aux = []
            size = len(queue)
            
            for v in range(size):
                root = queue.popleft()
                
                aux.append(root.val)
                
                if(root.left):
                    queue.append(root.left)
                if(root.right):
                    queue.append(root.right)
            
            ans.append(aux)
        
        return ans[::-1]