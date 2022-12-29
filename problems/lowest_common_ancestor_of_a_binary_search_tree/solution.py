# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return None

        cur=node.val

        if cur<p.val and cur<q.val:
            return self.lowestCommonAncestor(node.right, p, q)
        if cur>p.val and cur>q.val:
            return self.lowestCommonAncestor(node.left, p, q)

        return node