# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        ans = []
        if not root:
            return ans
        que = collections.deque([root])
        odd = False
        while que:
            ds = []
            for _ in range(len(que)):
                node = que.popleft()
                ds.append(node.val)
                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)
            if odd:
                ans.append(ds[::-1])
                odd = False
            else:
                ans.append(ds)
                odd = True
                
        
        return ans