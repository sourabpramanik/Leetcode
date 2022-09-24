# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ans = []
        self.inOrder(root, ans)
        return self.build(ans, 0, len(ans)-1)
        
    
    def inOrder(self, node, a):
        if not node:
            return
        
        self.inOrder(node.left, a)
        a.append(node.val)
        self.inOrder(node.right, a)
    
    def build(self, nums, s, e):        
        if s>e:
            return None
        mid = (s+e)//2

        root = TreeNode(nums[mid])
        root.left = self.build(nums, s, mid-1)
        root.right = self.build(nums, mid+1, e)

        return root