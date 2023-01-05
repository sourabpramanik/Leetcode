# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if not root:
            return ans
        queue=collections.deque([root])
        lev=1

        while queue:
            size=len(queue)
            temp=[]
            for _ in range(0, size):
                node=queue.popleft()
                if node:
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if lev%2==0:
                l=0
                r=len(temp)-1
                while l<=r:
                    temp[l], temp[r] = temp[r], temp[l]
                    l+=1
                    r-=1
            ans.append(temp[:])
            lev^=1

        return ans
