# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        ans = []
        if root is None: return ans
        queue = collections.deque([(root, 0)])
        tree = dict()
        
        while queue:
            tup = queue.popleft()
            node = tup[0]
            lev = tup[1]
            
            tree[lev] = node.val
            
            if node.left:
                queue.append((node.left, lev+1))
            if node.right:
                queue.append((node.right, lev+1))
        
        for v in tree.values():
            ans.append(v)
        return ans