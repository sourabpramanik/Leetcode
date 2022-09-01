# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count=0
        def pre(node, maxi):
            if not node: return None
            nonlocal count
            if(node.val>=maxi):
                maxi=node.val
                count+=1
            pre(node.left, maxi)
            pre(node.right, maxi)
        
                
        pre(root, float("-inf"))
        return count