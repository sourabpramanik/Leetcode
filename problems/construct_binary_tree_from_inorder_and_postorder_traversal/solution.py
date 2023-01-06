# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        store={}
        for i in range(0, len(inorder)):
            store[inorder[i]] = i
        
        return self.build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1, store)

    def build(self, postorder, pos, poe, inorder, ins, ine, store):
        if pos>poe or ins>ine:
            return None

        val=postorder[poe]
        x=store[val]
        numLeft=x-ins

        root=TreeNode(val)
        root.left=self.build(postorder, pos, pos+numLeft-1, inorder, ins, x-1, store)
        root.right=self.build(postorder, pos+numLeft, poe-1, inorder, x+1, ine, store)
        return root