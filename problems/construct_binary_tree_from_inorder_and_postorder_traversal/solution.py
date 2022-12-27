# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        nodes = dict()
        for i in range(0, len(inorder)):
            nodes[inorder[i]] = i
        return self.build(nodes, postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)
    
    def build(self, nodes, postorder, posStart, posEnd, inorder, iStart, iEnd):
        if posStart>posEnd or iStart>iEnd:
            return None
        
        val=postorder[posEnd]
        x=nodes[val]
        nEle=x-iStart
        root=TreeNode(val)
        root.left= self.build(nodes, postorder, posStart, posStart+nEle-1, inorder, iStart, x-1)
        root.right= self.build(nodes, postorder, posStart+nEle, posEnd-1, inorder, x+1, iEnd)
        return root