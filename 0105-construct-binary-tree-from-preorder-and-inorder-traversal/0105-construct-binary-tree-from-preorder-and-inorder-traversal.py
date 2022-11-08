# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        if len(preorder)==1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]
        idx = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])        
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        
        return root