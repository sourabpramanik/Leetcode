"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root: return res
        
        queue = collections.deque([root])
        
        while queue:
            size = len(queue)
            temp=[]
            for _ in range(size):
                node = queue.popleft()
                temp.append(node.val)
                if node.children:
                    queue.extend(node.children)                      
            
            
            res.append(temp)
        
        return res