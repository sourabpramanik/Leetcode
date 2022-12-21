# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=collections.deque([(root, 0)])
        maxW=0
        while queue:
            mini=queue[0][1]
            first=0 
            last=0
            size=len(queue)
            for i in range(0, size):
                node, ind = queue.popleft()
                ind = ind-mini
                if i==0:
                    first=ind
                if i==size-1:
                    last=ind
                                
                if node.left:
                    queue.append((node.left, ind*2+1))
                if node.right:
                    queue.append((node.right, ind*2+2))
            maxW=max(maxW, last-first+1)
        
        return maxW
