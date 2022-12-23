# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=collections.deque([root])
        level=1
        ans=[]
        while queue:
            size=len(queue)
            temp=[0]*size
            for i in range(0, size):
                node = queue.popleft()
                index = i if level%2 else size-i-1
                if node:
                    temp[index] = node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

            ans.append(temp)
            level^=1
        return ans