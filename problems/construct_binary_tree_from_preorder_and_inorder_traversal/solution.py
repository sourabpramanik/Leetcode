# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        nodes = dict()
        for i in range(0, len(inorder)):
            nodes[inorder[i]] = i
        return self.build(nodes, preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def build(self, nodes, preorder, preStart, preEnd, inorder, iStart, iEnd):
        if preStart>preEnd or iStart>iEnd:
            return None
        
        val=preorder[preStart]
        x=nodes[val]
        nEle=x-iStart
        root=TreeNode(val)
        root.left= self.build(nodes, preorder, preStart+1, preStart+nEle, inorder, iStart, x-1)
        root.right= self.build(nodes, preorder, preStart+nEle+1, preEnd, inorder, x+1, iEnd)
        return root