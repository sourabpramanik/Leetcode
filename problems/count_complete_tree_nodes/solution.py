# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        count=0
        
        if not root:
            return count
        
        while queue:
            node = queue.popleft()
            count+=1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return count