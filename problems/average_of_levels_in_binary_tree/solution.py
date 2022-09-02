# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans=[]
        queue= collections.deque([root])
        
        while(queue):
            size=len(queue)
            av=0
            c=0
            temp=collections.deque()
            for _ in range(size):
                node = queue.popleft()                
                
                if node:
                    av+=node.val
                    c+=1
                    node.left and temp.append(node.left)
                    node.right and temp.append(node.right)
                    
            ans.append(av/c)  
            queue=temp
            av=0
        
        return ans