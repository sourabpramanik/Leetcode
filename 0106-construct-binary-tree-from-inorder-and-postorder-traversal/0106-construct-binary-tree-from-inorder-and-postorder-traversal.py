# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder)==0 or len(inorder)==0:
            return None
        
        if len(inorder)==1:
            return TreeNode(postorder[0])
        
        val = postorder.pop(len(postorder)-1)
        idx = inorder.index(val)
        
        root = TreeNode(val)
    
        root.left = self.buildTree(inorder[:idx], postorder[:idx])        
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:])
        
        return root