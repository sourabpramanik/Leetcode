# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        arr = []
        if n==1:
            arr.append(TreeNode(0))
            return arr
        
        n = n-1
        
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n-i)
            
            for vl in left:
                for rl in right:
                    node = TreeNode(0)
                    node.left = vl                    
                    node.right = rl
                    arr.append(node)
        
        return arr