# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=collections.deque([root])
        ans=[]
        while queue:
            temp=[]
            size=len(queue)
            for _ in range(0, size):
                node = queue.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            ans.append(temp)
        
        return ans