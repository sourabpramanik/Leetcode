# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int,) -> str:        
        
        def dfs(node, target, ds):
            if node is None:
                return False
            
            if node.val == target:
                return True
            
            if node.left:
                if dfs(node.left, target, ds):
                    ds.appendleft("L")
                    return True
            
            if node.right:
                if dfs(node.right, target, ds):
                    ds.appendleft("R")
                    return True
            
        sq = collections.deque()
        dq = collections.deque()
        
        dfs(root, sv, sq)
        dfs(root, dv, dq)
        
        while sq and dq and sq[0] == dq[0]:
            sq.popleft()
            dq.popleft()
        
        return "U"*len(sq)+"".join(dq)
        
        
                
                