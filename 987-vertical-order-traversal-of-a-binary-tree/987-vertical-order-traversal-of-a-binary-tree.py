# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rec(self, X, Y, node, obj):
        
        if not node: return None
        obj[X].append((Y, node.val))
        
        self.rec(X-1, Y+1, node.left, obj)
        self.rec(X+1, Y+1, node.right, obj)
        
    def verticalTraversal(self, root):
        
        obj = defaultdict(list) 
        self.rec(0,0,root,obj)
        
        res=[]
        
        for i in sorted(obj.keys()):
            temp=[]            
            for j in sorted(obj[i]):
                temp.append(j[1])
            res.append(temp)
        
        return res
        
            
            