# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder=sorted(preorder)

        hashes={}

        for i in range(0, len(preorder)):
            hashes[inorder[i]] = i

        return self.build(hashes, preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build(self, hashes, preorder, preStart, preEnd, inorder, iStart, iEnd):
        if preStart>preEnd or iStart>iEnd:
            return None
        val=preorder[preStart]
        x=hashes[val]
        numleft=x-iStart
        root=TreeNode(val)
        root.left = self.build(hashes, preorder, preStart+1, preStart+numleft, inorder, iStart, x-1)    
        root.right = self.build(hashes, preorder, preStart+numleft+1, preEnd, inorder, x+1, iEnd)   
        return root 

        