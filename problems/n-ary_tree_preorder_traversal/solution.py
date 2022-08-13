"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        stk = [root]
        res = []
        
        if root is None: return res
        
        while stk:
            curr = stk.pop()
            res.append(curr.val)
            stk.extend(curr.children[::-1])
            
        return res