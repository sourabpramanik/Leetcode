# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        store={}
        for i in range(0, len(inorder)):
            store[inorder[i]]=i
        
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1, store)

    def build(self, preorder, prs, pre, inorder, ins, ine, store):
        if prs>pre or ins>ine:
            return None
        
        val = preorder[prs]
        x = store[val]
        numLeft=x-ins

        root=TreeNode(val)
        root.left=self.build(preorder, prs+1, prs+numLeft, inorder, ins, x-1, store)
        root.right=self.build(preorder, prs+numLeft+1, pre, inorder, x+1, ine, store)
        return root