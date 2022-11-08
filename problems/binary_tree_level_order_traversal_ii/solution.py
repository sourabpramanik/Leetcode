# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return  ans
        queue = collections.deque([root])
        
        while queue:
            ds=[]
            for _ in range(len(queue)):
                node=queue.popleft() 
                ds.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            ans.append(ds)
        
        return ans[::-1]