# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            n = TreeNode(val)
            n.left = root
            return n
        
        queue = collections.deque([root])        
        n=1
        while n < depth-1:
            temp = collections.deque()
            while queue:
                node = queue.popleft()
                
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            queue = temp
            n+=1
        while queue:
            node = queue.popleft()            
            t = node.left
            node.left = TreeNode(val)
            node.left.left = t

            t = node.right
            node.right = TreeNode(val)
            node.right.right = t         
                
            
        return root