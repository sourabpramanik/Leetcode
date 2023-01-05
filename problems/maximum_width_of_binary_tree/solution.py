# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=collections.deque([(root, 0)])
        ans=0
        while queue:
            size=len(queue)
            curMin=queue[0][1]
            first=0
            last=0
            for i in range(0, size):
                node, ind = queue.popleft()
                ind=ind-curMin
                if i==0:
                    first=ind
                if i==size-1:
                    last=ind
                
                if node.left:
                    queue.append((node.left, 2*ind+1))
                if node.right:
                    queue.append((node.right, 2*ind+2))
            ans=max(ans, last-first+1)
        
        return ans
