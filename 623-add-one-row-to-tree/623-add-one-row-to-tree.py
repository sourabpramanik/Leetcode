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
        
        stack = []                
        stack.append((root, 1))
        
        while len(stack)!=0:
            tup = stack.pop()
            node = tup[0]
            n = tup[1]
            if n==depth-1:
                t = node.left
                node.left = TreeNode(val)
                node.left.left = t
                
                t = node.right
                node.right = TreeNode(val)
                node.right.right = t
                
            else:
                if node.left:
                    stack.append((node.left, n+1))
                    
                if node.right:
                    stack.append((node.right, n+1))
                
            
            
        return root