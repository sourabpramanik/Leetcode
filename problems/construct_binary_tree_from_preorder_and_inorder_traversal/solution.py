# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recur(low, high):
            nonlocal preorder_index
            if low>high: return None
            
            x = TreeNode(preorder[preorder_index])
            mid = inorder_map[x.val]
            preorder_index+=1
            
            x.left = recur(low, mid-1)
            x.right = recur(mid+1, high)
            
            return x
        
        inorder_map = {}
        preorder_index=0
        
        for i, val in enumerate(inorder):
            inorder_map[val] = i
            
        return recur(0, len(preorder)-1)