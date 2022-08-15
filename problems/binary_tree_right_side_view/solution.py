# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        
        def recur(node, lev):
            if node is None: return ans
            
            if lev==len(ans):
                ans.append(node.val)
                
            recur(node.right, lev+1)
            recur(node.left, lev+1)
        
        recur(root, 0)
        
        return ans