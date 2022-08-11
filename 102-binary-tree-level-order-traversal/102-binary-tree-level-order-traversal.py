# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None: return []
        ls = deque([root])
        ans = []
        while len(ls)>0:
            aux, size = [], len(ls)
            for v in range(size):
                root = ls.popleft()           
                aux.append(root.val)

                if(root.left):
                    ls.append(root.left)
                if(root.right):
                    ls.append(root.right)
            ans.append(aux)
        return ans
                