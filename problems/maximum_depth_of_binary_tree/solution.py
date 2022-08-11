# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ls = deque([root])
        lev = 0
        aux = 1
        while len(ls)>0:
            cur = ls.popleft()           
            
            if(cur.left):
                ls.append(cur.left) 
            if(cur.right):
                ls.append(cur.right) 
            aux -= 1
            if aux==0:
                lev+=1
                aux = len(ls)
        return lev